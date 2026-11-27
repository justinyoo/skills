# Lay out slides using a PowerPoint template

English | [한국어](README.ko.md)

## What this skill is for

Place supplied wording, images, or data charts in the existing layouts of **one** local `.pptx` or `.potx` template. The result is a new `.pptx` that contains only the requested slides, without the template's example slides. If you have no template, you can explicitly choose the unbranded built-in template. The skill runs locally with Python and the `python-pptx` library. It does not write the talk or design a new theme.

See [SKILL.md](SKILL.md) for the full workflow, layout decisions, plan format, and prerequisites.

## Install with GitHub Copilot CLI

With GitHub Copilot CLI installed, run these commands in your terminal:

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install pptx-layout@justinyoo-skills
```

If you already registered the marketplace, skip the first command. If you installed the complete collection, this skill is already included.

For other agents, installation methods, and local checkouts, see the [Skills installation guide](../../docs/skills-installation-guide.md).

## Usage

In a GitHub Copilot CLI session, try:

```text
/pptx-layout Using "brand.potx", lay out one slide titled "Only production deployment still needs approval." Compare before and after for build, test, and deploy: before, all three required approval; after, only deploy does. Use the template's existing areas and save "approvals.pptx".
```
