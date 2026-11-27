"""Inspect PowerPoint layouts or fill existing placeholders. Run with --help."""

import argparse
import json
import math
import os
import sys
import warnings
from io import BytesIO
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import BadZipFile, ZipFile

from lxml import etree
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import PP_PLACEHOLDER as PH
from pptx.exc import PythonPptxError
from pptx.opc.constants import CONTENT_TYPE as CT, RELATIONSHIP_TYPE as RT
from pptx.oxml.shapes.picture import CT_Picture


class LayoutError(ValueError):
    """The template or placement plan cannot produce the requested slides."""


TEXT_TYPES = {PH.TITLE, PH.CENTER_TITLE, PH.SUBTITLE, PH.BODY, PH.OBJECT,
              PH.VERTICAL_BODY, PH.VERTICAL_OBJECT, PH.VERTICAL_TITLE}
IMAGE_TYPES = {PH.PICTURE, PH.OBJECT}


def load_template(path):
    if path is None:
        return Presentation()  # CLI requires --builtin explicitly
    if path.suffix.lower() not in {".pptx", ".potx"}:
        raise LayoutError("template must be a local .pptx or .potx")
    if not path.is_file():
        raise LayoutError(f"template not found: {path}")
    if path.suffix.lower() == ".pptx":
        return Presentation(str(path))

    # python-pptx accepts a presentation main part, not a template main part.
    buffer = BytesIO()
    with ZipFile(path) as source, ZipFile(buffer, "w") as target:
        manifest = etree.fromstring(
            source.read("[Content_Types].xml"),
            etree.XMLParser(resolve_entities=False, no_network=True),
        )
        main = manifest.findall(f'{{*}}Override[@ContentType="{CT.PML_TEMPLATE_MAIN}"]')
        if len(main) != 1:
            raise LayoutError("not a PowerPoint template package")
        main[0].set("ContentType", CT.PML_PRESENTATION_MAIN)
        for part in source.infolist():
            data = (etree.tostring(manifest) if part.filename == "[Content_Types].xml"
                    else source.read(part))
            target.writestr(part, data)
    buffer.seek(0)
    return Presentation(buffer)


def contents(slot):
    kind = slot.placeholder_format.type
    return ((["text"] if kind in TEXT_TYPES else [])
            + (["image", "chart"] if kind in IMAGE_TYPES else []))


def inventory(prs):
    layouts = []
    for master_id, master in enumerate(prs.slide_masters):
        for layout_id, layout in enumerate(master.slide_layouts):
            layouts.append({
                "master": master_id, "layout": layout_id, "name": layout.name,
                "slots": [{
                    "idx": s.placeholder_format.idx, "name": s.name,
                    "type": s.placeholder_format.type.name, "accepts": contents(s),
                    "box_emu": [s.left, s.top, s.width, s.height],
                } for s in layout.iter_cloneable_placeholders()],
            })
    return {"slide_size_emu": [prs.slide_width, prs.slide_height], "layouts": layouts}


def keys(obj, required, optional=()):
    if not isinstance(obj, dict):
        raise LayoutError("expected a JSON object")
    missing = set(required) - obj.keys()
    extra = obj.keys() - set(required) - set(optional)
    if missing or extra:
        raise LayoutError(f"missing fields {sorted(missing)}; unknown fields {sorted(extra)}")


def text(value):
    if not isinstance(value, str) or not value.strip():
        raise LayoutError("expected a nonempty string")
    return value


def integer(value):
    if type(value) is not int or value < 0:
        raise LayoutError(f"expected a nonnegative integer, got {value!r}")
    return value


def elements(value):
    if not isinstance(value, list) or not value:
        raise LayoutError("expected a nonempty array")
    return value


def chart_figure(spec, width, height):
    keys(spec, ["type", "categories", "series"], ["unit"])
    if spec["type"] not in ("bar", "line"):
        raise LayoutError("chart.type must be bar or line")
    labels = [text(x) for x in elements(spec["categories"])]
    series = elements(spec["series"])
    unit = text(spec["unit"]) if "unit" in spec else ""
    for s in series:
        keys(s, ["name", "values"])
        text(s["name"])
        values = elements(s["values"])
        if len(values) != len(labels) or any(
            type(v) not in (float, int) or not math.isfinite(v) for v in values
        ):
            raise LayoutError("each series needs one finite number per category")
    # Image-only and text-only plans do not need Matplotlib.
    try:
        from matplotlib.figure import Figure
    except ImportError as exc:
        raise LayoutError("data charts require matplotlib; install the chart dependency") from exc
    fig = Figure(figsize=(width / 914400, height / 914400), layout="constrained")
    ax = fig.subplots()
    for j, s in enumerate(series):
        if spec["type"] == "bar":
            step = 0.8 / len(series)
            pos = [i + (j - (len(series) - 1) / 2) * step for i in range(len(labels))]
            ax.bar(pos, s["values"], width=step, label=s["name"])
        else:
            ax.plot(range(len(labels)), s["values"], marker="o", label=s["name"])
    ax.set_xticks(range(len(labels)), labels)
    ax.set_ylabel(unit)
    ax.legend()
    # Let users name an installed font for the language of their chart labels.
    if font := os.environ.get("PPTX_LAYOUT_FONT"):
        from matplotlib import font_manager
        from matplotlib.text import Text
        font_manager.findfont(font_manager.FontProperties(family=font), fallback_to_default=False)
        for label in fig.findobj(match=Text):
            label.set_fontfamily(font)
    return fig


def picture(slot, blob, description):
    # Both PICTURE and generic OBJECT placeholders accept images in PowerPoint.
    # Some viewers ignore blipFill insets. Fit the picture rectangle itself
    # inside the inspected slot and preserve its idx rather than adding a shape.
    w, h = slot.width, slot.height
    if not w or not h or min(w, h) < 0:
        raise LayoutError("image slot has no usable dimensions")
    with Image.open(BytesIO(blob)) as image:
        iw, ih = image.size
        if image.format not in {"PNG", "JPEG"}:
            raise LayoutError("supply a PNG or JPEG image")
        image.verify()
    _, rid = slot.part.get_or_add_image_part(BytesIO(blob))
    pic = CT_Picture.new_ph_pic(slot.shape_id, "Picture", "", rid)
    pic.nvPicPr.cNvPr.set("name", slot.name)
    pic.nvPicPr.cNvPr.set("descr", description)
    scale = min(w / iw, h / ih)
    cw, ch = round(iw * scale), round(ih * scale)
    if (w, h) != (cw, ch):
        pic.x, pic.y = slot.left + (w - cw) // 2, slot.top + (h - ch) // 2
        pic.cx, pic.cy = cw, ch
    slot._replace_placeholder_with(pic)


def fill(slot, item, directory):
    fields = set(item) & {"text", "image", "chart"}
    if len(fields) != 1:
        raise LayoutError("specify exactly one of text, image or chart")
    kind = fields.pop()
    keys(item, ["idx", kind], ["alt"] if kind != "text" else [])
    if kind not in contents(slot):
        raise LayoutError(f"{kind} does not fit {slot.placeholder_format.type.name}")
    if kind == "text":
        slot.text = text(item[kind])
        return
    if kind == "image":
        path = directory / text(item[kind])
        blob = path.read_bytes()
        alt = text(item.get("alt", path.name))
    else:
        if not slot.width or not slot.height:
            raise LayoutError("chart slot has no dimensions")
        spec = item["chart"]
        fig = chart_figure(spec, slot.width, slot.height)
        stream = BytesIO()
        with warnings.catch_warnings():
            warnings.filterwarnings("error", message=r"Glyph .* missing from font")
            warnings.filterwarnings("error", message=r"[Cc]onstrained.layout not applied.*")
            try:
                fig.savefig(stream, format="png", dpi=160)
            except UserWarning as exc:
                raise LayoutError(f"{exc}; choose a larger slot or set PPTX_LAYOUT_FONT") from exc
        blob = stream.getvalue()
        alt = text(item["alt"]) if "alt" in item else "; ".join(
            f"{series['name']}: " + ", ".join(
                f"{label} {v}" for label, v in zip(spec["categories"], series["values"])
            ) for series in spec["series"]
        ) + (f" ({spec['unit']})" if "unit" in spec else "")
    picture(slot, blob, alt)


def remove_examples(prs):
    # python-pptx has no public slide removal API. Remove lists that reference
    # the old slides before releasing their relationships and reusing slide IDs.
    slides = prs.slides._sldIdLst
    for node in prs.part._element.xpath(
        "./p:custShowLst | .//p:extLst/*/*[local-name()='sectionLst']"
    ):
        node.getparent().remove(node)
    removed = set()
    for entry in list(slides):
        rid = entry.rId
        removed.add(prs.part.related_part(rid))
        slides.remove(entry)
        prs.part.drop_rel(rid)
    # Some templates keep independent references, e.g. viewProps' last slide.
    # View state, slide-show settings and thumbnails are optional for a new deck.
    for rel in list(prs.part.rels.values()):
        if rel.reltype in (RT.VIEW_PROPS, RT.PRES_PROPS):
            prs.part.rels.pop(rel.rId)
    for rel in list(prs.part.package._rels.values()):
        if rel.reltype in (RT.THUMBNAIL, RT.EXTENDED_PROPERTIES):
            prs.part.package._rels.pop(rel.rId)
    if removed.intersection(prs.part.package.iter_parts()):
        raise LayoutError("template contains a retained link to an example slide; "
                          "remove that link in a template copy before building")


def build(prs, plan, directory):
    keys(plan, ["slides"])
    slides = elements(plan["slides"])
    remove_examples(prs)
    for number, entry in enumerate(slides, 1):
        try:
            keys(entry, ["master", "layout", "slots"])
            master = prs.slide_masters[integer(entry["master"])]
            layout = master.slide_layouts[integer(entry["layout"])]
            slide = prs.slides.add_slide(layout)
            seen = set()
            for item in elements(entry["slots"]):
                if not isinstance(item, dict) or "idx" not in item:
                    raise LayoutError("each slot must specify idx")
                idx = integer(item["idx"])
                if idx in seen:
                    raise LayoutError(f"duplicate slot idx {idx}")
                seen.add(idx)
                try:
                    fill(slide.placeholders[idx], item, directory)
                except (ValueError, OSError, KeyError) as exc:
                    raise LayoutError(f"slot {idx}: {exc}") from exc
        except (IndexError, ValueError, KeyError) as exc:
            raise LayoutError(f"slide {number}: {exc}") from exc
    return prs


def save_new(prs, output):
    if output.suffix.lower() != ".pptx" or output.exists():
        raise LayoutError(f"output must be a new .pptx file: {output}")
    # Publish only a complete, reopened package; a concurrent output isn't replaced.
    with NamedTemporaryFile(dir=output.parent, suffix=".pptx", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        prs.save(tmp_path)
        result = Presentation(str(tmp_path))
        if len(result.slides) != len(prs.slides):
            raise LayoutError("saved slide count differs from the plan")
        os.link(tmp_path, output)
    finally:
        tmp_path.unlink()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("inspect", "build"):
        cmd = commands.add_parser(name)
        group = cmd.add_mutually_exclusive_group(required=True)
        group.add_argument("--template", type=Path, action="append")
        group.add_argument("--builtin", action="store_true")
        if name == "build":
            cmd.add_argument("--plan", type=Path, required=True)
            cmd.add_argument("--output", type=Path)
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        parser.print_help()
        return 0
    args = parser.parse_args(argv)
    if args.template and len(args.template) != 1:
        parser.error("use exactly one template file")
    try:
        source = args.template[0] if args.template else None
        prs = load_template(source)
        if args.command == "inspect":
            print(json.dumps(inventory(prs), ensure_ascii=False, indent=2))
        else:
            output = args.output or args.plan.with_name(args.plan.stem + "-layout.pptx")
            plan = json.loads(args.plan.read_text(encoding="utf-8"))
            save_new(build(prs, plan, args.plan.parent), output)
            print(output)
    except (OSError, ValueError, BadZipFile, KeyError, etree.XMLSyntaxError, PythonPptxError) as exc:
        parser.exit(1, f"pptx-layout: {exc}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
