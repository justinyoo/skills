# AGENTS.md

Guidance for AI coding agents working in this repository.

## What this repository is

This repository is a curated collection of **skills** for AI coding agents. A skill packages
domain-specific knowledge and, optionally, runnable scripts that an agent can read and execute to perform a well-defined task (for example, removing speaker notes from a PowerPoint file).

Agents discover a skill by reading its `SKILL.md`, then follow the instructions and invoke the bundled scripts as needed.

## Repository structure

```text
.
├── AGENTS.md             # Guidance for AI coding agents working in this repository
└── skills/
    └── <skill-name>/
        ├── SKILL.md      # Required: skill description and usage instructions
        └── scripts/      # Optional: supporting scripts the skill runs
```

- `skills/` is the source of truth. Use the standard installer as described in README.
- Each skill lives in its own directory under `skills/<skill-name>/`.
- `<skill-name>` is lowercase, hyphen-separated (kebab-case), e.g. `pptx-denote`.
- Every skill directory **must** contain a `SKILL.md`.
- Supporting code goes in a `scripts/` subdirectory inside the skill.
- Skills may include additional subdirectories for supporting resources, such as reference documents, templates, or rules, as documented in their `SKILL.md`.

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

1. Create `skills/<skill-name>/`.
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

## Repository maintenance

Maintain `README.md`, `marketplace.json`, and the skill keywords in `plugin.json` when adding, renaming, or removing a skill. The other host manifests point to the complete collection and canonical `skills/` directory.

Authoring helpers such as `create-skill` are external tools. Use an available installation or obtain approval to install one on demand; do not vendor the helper into this collection. Preserve repository-specific content when following an external generator's instructions.

CI installs the pinned Vally dependencies on its runner. Only dependency manifests, lockfiles, repository-specific checks, and link policy are committed. See `docs/repository-maintenance.md` for local equivalents. There is no managed-state directory, local repository generator, or GitHub Pages deployment.
