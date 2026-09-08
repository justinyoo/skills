# Create TRD

## What this skill is for

Create or update a technical requirements document (TRD) as a companion to a product requirements document (PRD). The skill translates product requirements into verifiable technical behavior, interfaces, qualities, and constraints through focused questions. A PRD is required before drafting; if one is missing, the skill asks whether to create it first.

See [SKILL.md](SKILL.md) for the full workflow and prerequisites.

## Install with GitHub Copilot CLI

With GitHub Copilot CLI installed, run these commands in your terminal:

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install create-trd@justinyoo-skills
```

If you already registered the marketplace, skip the first command. If you installed the complete collection, this skill is already included.

For other agents, installation methods, and local checkouts, see the [Skills installation guide](../../docs/skills-installation-guide.md).

## Usage

In a GitHub Copilot CLI session, try:

```text
/create-trd Create a TRD from PRD.md and interview me about the technical gaps.
```
