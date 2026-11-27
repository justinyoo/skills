"""Run from the skill directory: python -m unittest discover -s tests"""

import json
import subprocess
import sys
import tempfile
import unittest
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

from PIL import Image
from pptx import Presentation
from pptx.opc.constants import CONTENT_TYPE as CT

from scripts.layout import LayoutError, build, chart_figure, save_new


CLI = Path(__file__).resolve().parents[1] / "scripts" / "layout.py"
SERIES = {"type": "bar", "categories": ["Build", "Test", "Ship"],
          "unit": "minutes", "series": [{"name": "Before", "values": [8, 5, 4]},
                                        {"name": "After", "values": [4, 3, 4]}]}


def run(*args):
    return subprocess.run([sys.executable, CLI, *args], capture_output=True, text=True)


class LayoutTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.directory = Path(tmp.name)
        self.template = self.directory / "example.pptx"
        self.plan = self.directory / "plan.json"
        self.output = self.directory / "output.pptx"
        prs = Presentation()
        prs.slides.add_slide(prs.slide_layouts[0]).shapes.title.text = "Old sample"
        prs.save(self.template)
        self.potx = self.template.with_suffix(".potx")
        with ZipFile(self.template) as src, ZipFile(self.potx, "w") as dst:
            for part in src.infolist():
                data = src.read(part)
                if part.filename == "[Content_Types].xml":
                    data = data.replace(CT.PML_PRESENTATION_MAIN.encode(),
                                        CT.PML_TEMPLATE_MAIN.encode())
                dst.writestr(part, data)
        image = self.directory / "chart.png"
        Image.new("RGB", (350, 90), "#2b6ca0").save(image)
        self.slides = [
            {"master": 0, "layout": 4, "slots": [
                {"idx": 0, "text": "Automation removes two approvals"},
                {"idx": 1, "text": "Before"}, {"idx": 2, "text": "Build\nTest\nShip"},
                {"idx": 3, "text": "After"}, {"idx": 4, "text": "Auto\nAuto\nManual"},
            ]},
            {"master": 0, "layout": 3, "slots": [
                {"idx": 0, "text": "Build time fell the most"},
                {"idx": 1, "image": "chart.png", "alt": "Existing chart"},
                {"idx": 2, "chart": SERIES},
            ]},
        ]
        self.plan.write_text(json.dumps({"slides": self.slides}), encoding="utf-8")

    def test_pptx_potx_builtin_produce_requested_slides(self):
        for args in (["--template", self.template], ["--template", self.potx], ["--builtin"]):
            with self.subTest(args=args):
                original = args[1].read_bytes() if len(args) == 2 else None
                inspect = run("inspect", *args)
                self.assertEqual(inspect.returncode, 0, inspect.stderr)
                self.assertTrue(json.loads(inspect.stdout)["layouts"][4]["slots"])
                result = run("build", *args, "--plan", self.plan, "--output", self.output)
                self.assertEqual(result.returncode, 0, result.stderr)
                p = Presentation(str(self.output))
                self.assertEqual([s.shapes.title.text for s in p.slides],
                                 [s["slots"][0]["text"] for s in self.slides])
                self.assertEqual(len(p.slide_masters), 1)
                self.assertEqual(p.slides[0].slide_layout.part.partname,
                                 p.slide_layouts[4].part.partname)
                self.assertEqual(p.slides[0].placeholders[4].text, "Auto\nAuto\nManual")
                image = p.slides[1].placeholders[1]
                self.assertEqual(image.image.blob, (self.directory / "chart.png").read_bytes())
                self.assertEqual(image.left, p.slide_layouts[3].placeholders[1].left)
                self.assertEqual(image.width, p.slide_layouts[3].placeholders[1].width)
                self.assertGreater(image.top, p.slide_layouts[3].placeholders[1].top)
                self.assertAlmostEqual(image.width / image.height, 350 / 90, places=5)
                chart = p.slides[1].placeholders[2]
                with Image.open(BytesIO(chart.image.blob)) as rendered:
                    self.assertEqual(rendered.format, "PNG")
                    self.assertGreater(len(rendered.convert("RGB").getcolors(100000)), 20)
                with ZipFile(self.output) as out, ZipFile(self.template) as src:
                    self.assertEqual(out.read("ppt/theme/theme1.xml"), src.read("ppt/theme/theme1.xml"))
                    for filename in out.namelist():
                        if filename.startswith("ppt/slides/slide") and filename.endswith(".xml"):
                            self.assertNotIn(b"Old sample", out.read(filename))
                if original is not None:
                    self.assertEqual(args[1].read_bytes(), original)
                self.output.unlink()

    def test_bar_line_data_and_labels(self):
        for kind in ["bar", "line"]:
            with self.subTest(kind=kind):
                ax = chart_figure({**SERIES, "type": kind}, 5100000, 3800000).axes[0]
                values = ([list(line.get_ydata()) for line in ax.lines] if kind == "line"
                          else [[bar.get_height() for bar in bars] for bars in ax.containers])
                self.assertEqual(values, [[8, 5, 4], [4, 3, 4]])
                self.assertEqual([t.get_text() for t in ax.get_xticklabels()], SERIES["categories"])
                self.assertEqual(ax.get_ylabel(), "minutes")

    def test_no_fallback_or_overwrite(self):
        for args in [[], ["--template", self.template, "--builtin"],
                     ["--template", self.template, "--template", self.potx],
                     ["--template", self.directory / "missing.pptx"]]:
            result = run("build", *args, "--plan", self.plan, "--output", self.output)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(self.output.exists())
        original = self.template.read_bytes()
        result = run("build", "--template", self.template, "--plan", self.plan,
                     "--output", self.template)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(original, self.template.read_bytes())

    def test_invalid_plan_fails_without_publishing(self):
        for item in [{"idx": 90, "text": "bad"}, {"idx": 0, "chart": SERIES},
                     {"idx": 2, "chart": {**SERIES, "categories": ["mismatch"]}}]:
            with self.subTest(item=item):
                self.slides[1]["slots"] = [item]
                with self.assertRaisesRegex(LayoutError, "slide 2: slot"):
                    save_new(build(Presentation(), {"slides": self.slides}, self.directory),
                             self.output)
                self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main()
