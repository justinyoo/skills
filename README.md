# Skills for AI Coding Agents

A curated collection of **skills** for AI coding agents. A skill packages domain-specific knowledge and, optionally, runnable scripts that an agent can read and execute to perform a well-defined task — for example, removing speaker notes from a PowerPoint file.

Agents discover a skill by reading its `SKILL.md`, then follow the instructions and invoke the bundled scripts as needed.

> [!NOTE]
> Start with the [GitHub Copilot example](#installing-skills) below. See the [Skills installation guide](docs/skills-installation-guide.md) for other agents, installation scopes, local checkouts, and native marketplace/plugin methods.

## Repository structure

```text
.
├── AGENTS.md             # Guidance for AI coding agents working in this repository
└── skills/
    └── <skill-name>/
        ├── SKILL.md      # Required: skill description and usage instructions
        └── scripts/      # Optional: supporting scripts the skill runs
```

- Each skill lives in its own directory under `skills/<skill-name>/`.
- `<skill-name>` is lowercase, hyphen-separated (kebab-case), e.g. `pptx-denote`.
- Every skill directory **must** contain a `SKILL.md`.
- Supporting code goes in a `scripts/` subdirectory inside the skill.
- Skills may include additional subdirectories for supporting resources, such as reference documents, templates, or rules, as documented in their `SKILL.md`.

## Available skills

| Skill                                                    | Description |
| -------------------------------------------------------- | ----------- |
| [`create-prd`](skills/create-prd/SKILL.md)       | Generate or update a product requirements document (PRD) from user-provided context and interviews to fill missing details. |
| [`create-tdd`](skills/create-tdd/SKILL.md)       | Generate or update a technical design document (TDD) from a required PRD and TRD through design proposals and adaptive interviews, with references to existing ADRs. |
| [`create-trd`](skills/create-trd/SKILL.md)       | Generate or update a technical requirements document (TRD) as a PRD companion through adaptive interviews, asking to create a PRD first when missing. |
| [`localizations`](skills/localizations/SKILL.md) | Localize content into the supported target locales using locale-specific rules. |
| [`pptx-denote`](skills/pptx-denote/SKILL.md)     | Remove all slide notes from a PowerPoint presentation using the `python-pptx` library. |

## Using a skill

1. Install the skills for your agent using the instructions below.
1. Open the skill's `SKILL.md` and read the **How it works** section.
1. Ask your agent to use the skill.

   For example, ask GitHub Copilot CLI:

    ```text
    Use the pptx-denote skill to remove speaker notes from "my-presentation.pptx".
    ```

## Installing skills

With GitHub Copilot CLI installed, add this repository as a marketplace, then install the collection's plugin from it:

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install justinyoo-skills@justinyoo-skills
```

The `justinyoo-skills` plugin includes all skills in this collection. Alternatively, after registering the marketplace, browse and install an individual skill:

```sh
copilot plugin marketplace browse justinyoo-skills
copilot plugin install <skill-name>@justinyoo-skills
```

Replace `<skill-name>` with a listed name, such as `create-prd`. Choose the collection or individual plugins to avoid installing the same skill twice. For direct plugin installation, the `npx skills` method, local checkouts, and other coding agents, see the [installation guide](docs/skills-installation-guide.md).

## Adding a new skill

### Assisted authoring with `create-skill` (recommended)

Use the external `create-skill` skill with your coding agent. Reuse an installation already available to the agent; if it is missing, obtain approval before installing it on demand. For GitHub Copilot:

```sh
npx skills add jongio/skills --skill create-skill -g --agent github-copilot
```

For other agent identifiers, see the [installation guide](docs/skills-installation-guide.md#install-with-the-skills-cli). Then ask your agent to use `create-skill`, for example:

```text
Use create-skill to create a skill named <skill-name> for <task>.
Use this repository's skills/ layout and preserve its existing custom content.
```

Let the skill collect missing requirements and produce a dry-run preview. Review the proposed files, target paths, prerequisites, and registration changes before approving the exact plan. Keep the helper external: do not add a bundled `create-skill` installation, repository-management framework, or authoring step to CI.

### Manual authoring (fallback)

If the helper is unavailable or you prefer to author the skill directly:

1. Create `skills/<skill-name>/`.
2. Add a `SKILL.md` with valid YAML frontmatter (`name`, `description`).
3. Place any executable code under `scripts/` and document the exact invocation in `SKILL.md`.
4. List prerequisites (libraries, tools) and how to install them.
5. Keep the skill self-contained, single-purpose, and idempotent where possible.

With either method, add a matching `plugin.json` inside the skill directory for individual Copilot plugin installation, and keep the [available-skills table](#available-skills), [marketplace registration](marketplace.json), and skill keywords in the collection's [plugin.json](plugin.json) consistent with the new skill. See [AGENTS.md](AGENTS.md) for the full set of conventions.

## Contributing

Contributions of new skills are welcome. Follow the conventions in [AGENTS.md](AGENTS.md) and keep each skill focused on a single, well-defined task.

## Repository maintenance

See [repository maintenance](docs/repository-maintenance.md) for CI validation and on-demand authoring tools.

This repository contains the authored skills and their distribution manifests, not a bundled repository generator or `create-skill` installation. GitHub Actions installs the pinned validation tools into its temporary runner directory. GitHub Pages is not configured.
