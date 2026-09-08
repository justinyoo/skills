# Skills for AI Coding Agents

A curated collection of **skills** for AI coding agents. A skill packages domain-specific knowledge and, optionally, runnable scripts that an agent can read and execute to perform a well-defined task — for example, removing speaker notes from a PowerPoint file.

Agents discover a skill by reading its `SKILL.md`, then follow the instructions and invoke the bundled scripts as needed.

> [!NOTE]
> Install individual skills with the [skills CLI](#install-with-the-skills-cli), or install the collection through your agent's [native marketplace, plugin, or extension workflow](#install-through-marketplaces-and-plugins). Choose one method per agent to avoid duplicate skill installations.

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
1. Run a prompt with the slash (`/`) command.

   For example, after installing with the skills CLI, remove notes from a PowerPoint file with:

    ```
    /pptx-denote <my-pptx-file-to-remove-notes>.pptx
    ```

Native plugins can namespace skill names. See the agent-specific instructions below; for example, Claude Code exposes this skill as `/justinyoo-skills:pptx-denote` when installed as part of the plugin.

## Install with the skills CLI

From the project where you want to use these skills, run the standard [skills installer](https://github.com/vercel-labs/skills). Node.js and npm are required; `npx` runs the installer on demand:

### GitHub Copilot

```sh
npx skills add justinyoo/skills --skill '*' --agent github-copilot
```

### Claude Code

[Claude Code](https://code.claude.com/docs/en/overview) uses the same installer with a different agent selection:

```sh
npx skills add justinyoo/skills --skill '*' --agent claude-code
```

Both commands install into the current project by default. Add `-g` for a user-wide installation across projects, or replace `'*'` with a specific skill name. The installer also supports agent identifiers such as `codex`, `cursor`, and `gemini-cli`; use the appropriate value for `--agent`.

### Using a local checkout

To install the skills from this checkout rather than the remote repository, run from the repository root:

```sh
npx skills add . --skill '*' --agent github-copilot
```

Use `--agent claude-code` for Claude Code. Always author changes under `skills/`, not in installer-managed copies. Cloning the repository alone does not install the skills for an agent.

## Install through marketplaces and plugins

The collection's plugin/extension identifier is **`justinyoo-skills`**. Its marketplace identifier is also **`justinyoo-skills`**. The native flows below install the complete collection; use the skills CLI when you want to select individual skills.

Use a current agent version with the relevant plugin support, and review its trust prompts. Organization policies may restrict custom marketplaces or local plugins. These files define this repository's own distribution sources; they do not imply a listing in any vendor's public marketplace.

### GitHub Copilot CLI

Install the collection directly from GitHub:

```sh
copilot plugin install justinyoo/skills
```

Alternatively, register this repository as a marketplace, browse it, and install the collection:

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin marketplace browse justinyoo-skills
copilot plugin install justinyoo-skills@justinyoo-skills
```

Use `copilot plugin list` to inspect installed plugins. These are terminal commands; inside an interactive Copilot CLI session, the equivalent commands begin with `/plugin`. See [Copilot's plugin installation guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing).

### Claude Code CLI

Inside an interactive Claude Code session, add the marketplace and install its collection plugin:

```text
/plugin marketplace add justinyoo/skills
/plugin install justinyoo-skills@justinyoo-skills
```

Open `/plugin` to review the installed plugin and its scope. Follow any reload instruction shown by the installer, or start a new session. Plugin skills are namespaced, for example:

```text
/justinyoo-skills:create-prd Create a PRD for my project.
```

The marketplace is defined in [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json). See [Claude Code's marketplace installation guide](https://code.claude.com/docs/en/discover-plugins).

### Codex CLI and ChatGPT desktop

Register the repository marketplace from the terminal:

```sh
codex plugin marketplace add justinyoo/skills
codex plugin marketplace list
```

In an interactive Codex CLI session, run `/plugins`, select the **Skills for AI Coding Agents** marketplace, and install **justinyoo-skills**. Start a new session to use its bundled skills.

For a local checkout opened in Codex in the ChatGPT desktop app, [`.agents/plugins/marketplace.json`](.agents/plugins/marketplace.json) supplies the repo-scoped marketplace. Restart the app after adding or changing the local marketplace, then select it in **Plugins** and install the collection. Repo/personal marketplace availability depends on the surface and workspace policy; this is separate from the public plugin directory.

See OpenAI's [marketplace setup reference](https://developers.openai.com/plugins/build/plugins#add-a-marketplace-from-the-cli) and [plugin installation guide](https://learn.chatgpt.com/docs/plugins). Native plugins are not available in the Codex IDE extension; use the skills installer for that workflow.

### Cursor

Cursor supports this repository's root [Agent Plugin manifest](plugin.json). Its documented native marketplace flow uses the UI:

1. On a Teams or Enterprise plan, open **Dashboard > Plugins > Team Marketplaces > Add Marketplace** and choose **Import from Repo**.
2. Enter `https://github.com/justinyoo/skills`, review **justinyoo-skills**, and configure marketplace access. Enterprise may require an administrator.
3. In Cursor, open **Customize**, find the collection in the team marketplace, and select **Install**.

For local use without a team marketplace, place the repository's plugin files under `<home>/.cursor/plugins/local/justinyoo-skills/`, keeping `plugin.json` and `skills/` at that directory's root. Restart Cursor or run **Developer: Reload Window**, then inspect **Customize**. This requires local plugin imports to be allowed by your organization. The skills CLI is another option when local or team plugins are unavailable.

See [Cursor's plugin and marketplace guide](https://cursor.com/docs/plugins).

### Gemini CLI

Gemini packages the collection as an extension using [gemini-extension.json](gemini-extension.json). From a terminal, with Git available:

```sh
gemini extensions install https://github.com/justinyoo/skills
```

Restart Gemini CLI after installation, then use `/extensions list` in the interactive session to inspect **justinyoo-skills**. Extension management commands such as `gemini extensions install` run in the terminal, not inside the interactive session. See [Gemini CLI's extension reference](https://geminicli.com/docs/extensions/reference/).

### Trying native plugins from a local checkout

For Copilot CLI, Claude Code, and Codex, replace `justinyoo/skills` with `.` in their **marketplace add** command while working at this repository's root, then install through the same marketplace flow. For Gemini, use `gemini extensions install .`. Cursor's local-plugin directory flow is described above.

## Adding a new skill

### Assisted authoring with `create-skill` (recommended)

Use the external `create-skill` skill with your coding agent. Reuse an installation already available to the agent; if it is missing, obtain approval before installing it on demand. For GitHub Copilot:

```sh
npx skills add jongio/skills --skill create-skill -g --agent github-copilot
```

Use `--agent claude-code` for Claude Code. Then ask your agent to use `create-skill`, for example:

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

With either method, keep the [available-skills table](#available-skills), [marketplace registration](marketplace.json), and skill keywords in [plugin.json](plugin.json) consistent with the new skill. See [AGENTS.md](AGENTS.md) for the full set of conventions.

## Contributing

Contributions of new skills are welcome. Follow the conventions in [AGENTS.md](AGENTS.md) and keep each skill focused on a single, well-defined task.

## Repository maintenance

See [repository maintenance](docs/repository-maintenance.md) for CI validation and on-demand authoring tools.

This repository contains the authored skills and their distribution manifests, not a bundled repository generator or `create-skill` installation. GitHub Actions installs the pinned validation tools into its temporary runner directory. GitHub Pages is not configured.
