# AGENTS.md

Guidance for AI coding agents working in this repository.

## What this repository is

This repository is a curated collection of **skills** for AI coding agents. A skill packages
domain-specific knowledge and, optionally, runnable scripts that an agent can read and execute to perform a well-defined task (for example, removing speaker notes from a PowerPoint file).

Agents discover a skill by reading its `SKILL.md`, then follow the instructions and invoke the bundled scripts as needed.

## Repository structure

```text
.
└── .github/
    └── skills/
        └── <skill-name>/
            ├── SKILL.md      # Required: skill description and usage instructions
            └── scripts/      # Optional: supporting scripts the skill runs
```

- Each skill lives in its own directory under `.github/skills/<skill-name>/`.
- `<skill-name>` is lowercase, hyphen-separated (kebab-case), e.g. `pptx-denote`.
- Every skill directory **must** contain a `SKILL.md`.
- Supporting code goes in a `scripts/` subdirectory inside the skill.

## SKILL.md conventions

Each `SKILL.md` starts with YAML frontmatter followed by Markdown documentation.

```markdown
---
name: <skill-name>
description: A one-sentence summary of what the skill does and when to use it.
---

# Human-readable title

Short overview of the skill.

## How it works

Explain the inputs, outputs, and behavior. Include the exact commands to run,
any prerequisites (e.g. required packages), and sensible defaults.
```

Frontmatter rules:

- `name` — must match the skill directory name exactly.
- `description` — concise and trigger-oriented; it is how an agent decides whether the
  skill applies to the current task.

## Adding a new skill

1. Create `.github/skills/<skill-name>/`.
2. Add a `SKILL.md` with valid frontmatter (`name`, `description`) following the convention above.
3. Place any executable code under `scripts/` and document the exact invocation in `SKILL.md`.
4. List prerequisites (libraries, tools) and how to install them.
5. Keep the skill self-contained, single-purpose, and idempotent where possible.

## Conventions for scripts

- Prefer small, focused, single-purpose scripts.
- Include a usage docstring/header and print help when run without arguments.
- Validate inputs and fail fast with clear error messages.
- Use sensible default output names rather than overwriting inputs.
- State runtime dependencies in `SKILL.md` (this repo does not pin a global dependency manifest).
- Style guide
  - If a script is written in Python, it should follow the [Style Guild for Python Code](https://peps.python.org/pep-0008/).
  - If a script is written in JavaScript, it should follow the [Guidelines for writing JavaScript code examples](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Code_style_guide/JavaScript).
  - If a script is written in TypeScript, it should follow the [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html).
  - If a script is written for bash, it should follow the [Shell Style Guide](https://google.github.io/styleguide/shellguide.html).

## Notes for agents

- Read the relevant `SKILL.md` before running any script in a skill.
- Run scripts from the skill directory using the documented command.
- Do not invent file paths or commands; rely on what each `SKILL.md` specifies.
