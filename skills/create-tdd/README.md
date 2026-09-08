# Create TDD

## What this skill is for

Create or update a technical design document (TDD) from a product requirements document (PRD) and a technical requirements document (TRD). The skill investigates available context, proposes solutions with tradeoffs, and asks focused questions to develop a design that satisfies the requirements. Both a PRD and a TRD are required before drafting; here, TDD means technical design document, not test-driven development.

See [SKILL.md](SKILL.md) for the full workflow and prerequisites.

## Install with GitHub Copilot CLI

With GitHub Copilot CLI installed, run these commands in your terminal:

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install create-tdd@justinyoo-skills
```

If you already registered the marketplace, skip the first command. If you installed the complete collection, this skill is already included.

For other agents, installation methods, and local checkouts, see the [Skills installation guide](../../docs/skills-installation-guide.md).

## Usage

In a GitHub Copilot CLI session, try:

```text
/create-tdd Design the solution for PRD.md and TRD.md, using the existing code.
```
