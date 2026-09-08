# Remove PowerPoint slide notes

## What this skill is for

Remove slide notes from a PowerPoint (`.pptx`) presentation and save a new file with the same slides but without the notes. Use it to prepare a copy for sharing without speaker notes. The skill uses Python and the `python-pptx` library; by default, the output filename adds `-denoted` to the original name.

See [SKILL.md](SKILL.md) for the full workflow and prerequisites.

## Install with GitHub Copilot CLI

With GitHub Copilot CLI installed, run these commands in your terminal:

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install pptx-denote@justinyoo-skills
```

If you already registered the marketplace, skip the first command. If you installed the complete collection, this skill is already included.

For other agents, installation methods, and local checkouts, see the [Skills installation guide](../../docs/skills-installation-guide.md).

## Usage

In a GitHub Copilot CLI session, try:

```text
/pptx-denote Remove all slide notes from "community-meetup.pptx".
```
