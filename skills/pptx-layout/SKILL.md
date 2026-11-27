---
name: pptx-layout
description: Place supplied text, images, or data charts in the existing layouts of a PowerPoint template; use for arranging slide content, comparisons, and steps, not for writing a talk or designing a template.
metadata:
  version: "1.1.2"
---

# Lay out slide content in a PowerPoint template

Use this skill to create a new `.pptx` that contains only the requested slides. The output reuses the selected template's slide size, masters, layouts, theme, and placeholders. Do not design new layouts, invent a storyline, prescribe a slide count or speaking time, or copy the template's example slides into the output.

## How it works

1. **Choose one source.** One template file is enough: either a local `.pptx` or a local `.potx`. If the user provides several candidates without choosing one, ask which to use; never merge templates. If no file is provided, ask **once** whether the user will supply a file or wants the unbranded built-in template, and do not create a file until they answer. If the user has already chosen the built-in template, use it without asking again. A missing, damaged, or unsupported file is an error, not permission to fall back to the built-in template.
2. **Inspect before choosing a layout.** Run the `inspect` command below and consider every master. Base decisions on slot types, positions, and dimensions; treat layout names and example slides only as hints. Master and layout IDs come from the inspected template, not from English layout names or an assumed list order. A placeholder's `idx` is its identifier, **not** its position in the list. Use the same unchanged source file for `inspect` and `build`.
3. **Match relationships, not counts.** Start from the slide message and wording the user supplied. If either is not established, clarify it before building; do not write the talk. Apply the 1/2/3 guide below. In the placement plan, map each piece of supplied content to a separate compatible slot. Keep any supplied image or figure as is. If the user supplies only numbers and a chart supports the message, render the numbers as a chart image.
4. **Check the fit before building.** Prefer one large evidence slot to two slots too small to read. If no existing layout can express three stages, use a numbered list in a body slot. If the content still does not fit, propose splitting it across slides, and confirm any change to the approved wording or the requested slides. Do not add free-standing shapes, silently omit content, or shrink the theme font. Do not assume that a template whose example slides use only free text boxes has fillable placeholders.
5. **Build and review.** Generate the new `.pptx`. Confirm that it opens, contains only the requested slides, and uses the intended layouts. Check the rendered slides for clipped text, cropped images or labels, reading order, and misleading comparisons, and check each chart against the source values and units. If no slide renderer is available, report the structural checks separately and do not claim that a visual review was performed.

## The 1/2/3 layout guide

| Question | Placement decision |
|---|---|
| **1 message:** What does this slide show? | Use one conclusion as the content slide's title, and keep only the evidence for that conclusion. A title slide or section divider does not need to make a claim. |
| **2 areas:** Is this a comparison or a claim with evidence? | For before and after, compare the two subjects against the **same criteria in the same order**. For an explanation with evidence, put short text in one slot and a figure large enough to read in the other. A single strong piece of evidence can use one slot. |
| **3 points:** Are these peers or steps? | Three comparable features can use three existing peer slots. Sequential steps use the template's process layout or a numbered list. Fewer than three points is fine. Three points do not require three columns, and a required fourth item must not be dropped. |

For example, under the title **“Only production deployment still needs approval,”** use **two** before-and-after columns, each showing the same **three** criteria: build, test, and deploy. If the same three terms instead support the message **“The release passes through three stages,”** present them as a sequence. Neither case requires moving a placeholder.

## Local commands

Use Python 3.10 or later, and install the dependencies in a virtual environment. The placeholder and packaging operations support `python-pptx` 1.0.2. Matplotlib is required only to render charts from data. Run the commands from this skill directory, and use absolute paths for user files when necessary:

```sh
python -m pip install "python-pptx==1.0.2"
python -m pip install matplotlib
python scripts/layout.py inspect --template "/path/to/brand.potx"
python scripts/layout.py build --template "/path/to/brand.potx" --plan "/path/to/layout.json" --output "/path/to/result.pptx"
```

A `.pptx` template works in place of the `.potx`. If the user explicitly chooses the built-in template, replace `--template "/path/to/brand.potx"` with `--builtin` **in both commands**. If you omit `--output`, the output is saved as `<plan-stem>-layout.pptx` next to the plan. Existing files, including the source template, are never overwritten. Relative image paths are resolved from the plan file's directory, not the current working directory.

### Placement plan

The following JSON assumes that inspection returned master `0` and layout `3`, with a `TITLE` placeholder at idx `0` and two `OBJECT` placeholders at idx `1` and `2`. Use the IDs from **your** inspection output. In that output, `box_emu` is `[left, top, width, height]`, where 914400 EMU equals 1 inch.

```json
{
  "slides": [{
    "master": 0,
    "layout": 3,
    "slots": [
      {"idx": 0, "text": "Build time decreased the most"},
      {"idx": 1, "text": "Build: 8 to 4 minutes\nTest: 5 to 3 minutes\nDeploy: unchanged"},
      {"idx": 2, "chart": {
        "type": "bar", "unit": "minutes",
        "categories": ["Build", "Test", "Deploy"],
        "series": [
          {"name": "Before", "values": [8, 5, 4]},
          {"name": "After", "values": [4, 3, 4]}
        ]
      }}
    ]
  }]
}
```

Give each slot exactly one of `text`, `image`, or `chart`. To use an existing chart image instead of data, **replace** the chart entry rather than adding to it: `{"idx": 2, "image": "before-after.png", "alt": "Build takes four fewer minutes after automation"}`. PNG and JPEG images are supported, and their original bytes are embedded without redrawing. In text slots, each newline starts a new paragraph. For data charts, use `bar` to compare categories and `line` to show an ordered trend. List the categories in their actual order, and give each series one finite value per category. Do not infer missing values or units. For labels in non-Latin scripts, set `PPTX_LAYOUT_FONT` to an installed font that contains the required glyphs, for example `PPTX_LAYOUT_FONT="Apple SD Gothic Neo"` on a Mac with that font.

Both supplied images and data charts are inserted as **pictures**, not editable PowerPoint charts. Each image is scaled to fit its `PICTURE` or generic `OBJECT` placeholder without cropping axes or legends. If objects retained from the template still link to its example slides, the build stops with an error; use a clean copy of the template. Error messages name the slide or input where applicable. Correct the input rather than silently modifying the template.

## Maintainer tests

These tests are not required to use the skill. After changing `scripts/layout.py`, install the dependencies above and run the deterministic, file-based tests from this skill directory:

```sh
python -m unittest discover -s tests
```
