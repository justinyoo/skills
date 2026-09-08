# AGENTS.md

Guidance for AI coding agents working in this repository.

## What this repository is

This repository is a curated collection of **skills** for AI coding agents. A skill packages domain-specific knowledge and, optionally, runnable scripts that an agent can read and execute to perform a well-defined task (for example, removing speaker notes from a PowerPoint file).

Agents discover a skill by reading its `SKILL.md`, then follow the instructions and invoke the bundled scripts as needed.

## Repository structure

```text
.
├── AGENTS.md             # Guidance for AI coding agents working in this repository
├── docs/                 # Installation and maintenance guides
└── skills/
    └── <skill-name>/
        ├── README.md     # Required: human-facing overview, installation, and usage
        ├── SKILL.md      # Required: skill description and usage instructions
        ├── plugin.json   # Required: individual Copilot plugin metadata
        ├── thumbnail.png # Optional: rendered thumbnail
        ├── thumbnail.svg # Optional: editable thumbnail source
        └── scripts/      # Optional: supporting scripts the skill runs
```

- `skills/` is the source of truth; make authored changes there, not in installation copies. Use one of the methods in the [Skills installation guide](docs/skills-installation-guide.md) to consume the skills.
- Each skill lives in its own directory under `skills/<skill-name>/`.
- `<skill-name>` is lowercase, hyphen-separated (kebab-case), e.g. `pptx-denote`.
- Every skill directory **must** contain `README.md`, `SKILL.md`, and `plugin.json`. The skill frontmatter name and plugin name must match the directory.
- Supporting code goes in a `scripts/` subdirectory inside the skill.
- Skills may include additional subdirectories for supporting resources, such as reference documents, templates, or rules, as documented in their `SKILL.md`.

## README.md conventions

Each skill's README is a short human-facing landing page with a descriptive title and three sections:

- **What this skill is for**: Explain the purpose, expected result, and any essential prerequisites or boundaries. Link to `SKILL.md` for the authoritative workflow rather than duplicating agent instructions.
- **Install with GitHub Copilot CLI**: Show terminal commands to register `justinyoo/skills` with `copilot plugin marketplace add`, then install the specific skill with `copilot plugin install <skill-name>@justinyoo-skills`. Explain that marketplace registration is only needed once and the complete collection already includes the skill. Link to `../../docs/skills-installation-guide.md` for other agents, installation methods, and local checkouts.
- **Usage**: Show one realistic, copyable `/<skill-name>` prompt in a `text` code block, to run in a GitHub Copilot CLI session. Include required inputs in the example and keep additional examples, options, and detailed workflows in `SKILL.md`.

Use the actual skill name in copyable commands. The root README's available-skills table links to each skill's `README.md`, not its `SKILL.md`.

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

Explain the inputs, outputs, and behavior. Include the exact commands to run, any prerequisites (e.g. required packages), and sensible defaults.
```

Frontmatter rules:

- `name` — must match the skill directory name exactly.
- `description` — concise and trigger-oriented; it is how an agent decides whether the
  skill applies to the current task.

## Adding a new skill

Prefer the external `create-skill` assisted workflow described in [README](README.md#adding-a-new-skill). Reuse an available installation, or obtain approval to install it on demand. Review its dry-run and approve only the intended files, paths, prerequisites, and registration changes. Do not vendor the helper or add authoring to CI.

Manual authoring is the fallback. Both methods must satisfy these requirements:

1. Create `skills/<skill-name>/`.
2. Add a `SKILL.md` with valid frontmatter (`name`, `description`) following the convention above.
3. Add a `README.md` following the human-facing overview, installation, and usage conventions above.
4. Add `plugin.json` with the same skill name, a version matching its marketplace entry, and `"skills": "./"` to expose the root `SKILL.md` as an individual Copilot plugin.
5. Place any executable code under the skill's `scripts/` directory and document the exact invocation in `SKILL.md`.
6. List prerequisites (libraries, tools) and how to install them.
7. Keep the skill self-contained, single-purpose, and idempotent where possible.
8. Complete the [skill-change checklist](docs/repository-maintenance.md#skill-change-checklist), whether the helper generated the files or they were written manually.

## Conventions for scripts

- Prefer small, focused, single-purpose scripts.
- Include a usage docstring/header and print help when run without arguments.
- Validate inputs and fail fast with clear error messages.
- Use sensible default output names rather than overwriting inputs.
- State each skill's runtime dependencies in its `SKILL.md`. The separate `.github/tools/vally/` manifest pins validation tooling, not the dependencies needed to execute skills.
- Keep any skill-level `npm test` command deterministic and free of model calls; model-based evaluations are separate, explicitly authorized work.
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

Use [repository maintenance](docs/repository-maintenance.md) for the metadata checklist and validation commands. Keep the collection plugin and individual skill plugins distinct; other host manifests expose the complete collection.

Run repository tests from the root with `node --test` on Node.js 24 or newer; they do not require an npm install. Static skill linting additionally needs the pinned Vally dependencies. CI installs those dependencies in its temporary runner directory, runs repository tests and static linting, and runs deterministic npm tests for skills that have `package.json`.

Only dependency manifests, lockfiles, repository-specific checks, and link policy are committed for validation. Preserve custom repository content. Do not introduce a managed-state directory, vendored authoring tools, model-based CI evaluations, or a GitHub Pages deployment.
