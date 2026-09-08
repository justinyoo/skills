# Skills installation guide

Install the [skills in this collection](../README.md#available-skills) with the standard skills CLI or your agent's native marketplace, plugin, or extension workflow. Choose one method per agent to avoid duplicate skill installations.

## Install with the skills CLI

From the project where you want to use these skills, run the standard [skills installer](https://github.com/vercel-labs/skills). Node.js and npm are required; `npx` runs the installer on demand.

For GitHub Copilot:

```sh
npx skills add justinyoo/skills --skill '*' --agent github-copilot
```

This command installs into the current project by default. Add `-g` for a user-wide installation across projects, or replace `'*'` with a specific skill name.

For other coding agents, use the same command with the appropriate `--agent` identifier from the installer's [supported agents list](https://github.com/vercel-labs/skills/blob/main/README.md#supported-agents).

### Using a local checkout

To install the skills from this checkout rather than the remote repository, run from the repository root:

```sh
npx skills add . --skill '*' --agent github-copilot
```

The same `--agent` selection applies to local installations. Always author changes under `skills/`, not in installer-managed copies. Cloning the repository alone does not install the skills for an agent.

## Install through marketplaces and plugins

The collection's plugin/extension identifier is **`justinyoo-skills`**. Its marketplace identifier is also **`justinyoo-skills`**. Copilot's marketplace additionally offers each skill as an individual plugin named after the skill; the skills CLI also supports selecting individual skills.

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

To install individual skills instead, use the registered marketplace:

```sh
copilot plugin marketplace browse justinyoo-skills
copilot plugin install <skill-name>@justinyoo-skills
```

Replace `<skill-name>` with a listed name, for example `create-prd`. Each `skills/<skill-name>/plugin.json` points to that directory's skill. Choose the complete collection or individual plugins to avoid duplicate installations.

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

The marketplace is defined in [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json). See [Claude Code's marketplace installation guide](https://code.claude.com/docs/en/discover-plugins).

### Codex CLI and ChatGPT desktop

Register the repository marketplace from the terminal:

```sh
codex plugin marketplace add justinyoo/skills
codex plugin marketplace list
```

In an interactive Codex CLI session, run `/plugins`, select the **Skills for AI Coding Agents** marketplace, and install **justinyoo-skills**. Start a new session to use its bundled skills.

For a local checkout opened in Codex in the ChatGPT desktop app, [`.agents/plugins/marketplace.json`](../.agents/plugins/marketplace.json) supplies the repo-scoped marketplace. Restart the app after adding or changing the local marketplace, then select it in **Plugins** and install the collection. Repo/personal marketplace availability depends on the surface and workspace policy; this is separate from the public plugin directory.

See OpenAI's [marketplace setup reference](https://developers.openai.com/plugins/build/plugins#add-a-marketplace-from-the-cli) and [plugin installation guide](https://learn.chatgpt.com/docs/plugins). Native plugins are not available in the Codex IDE extension; use the skills installer for that workflow.

### Cursor

Cursor supports this repository's root [Agent Plugin manifest](../plugin.json). Its documented native marketplace flow uses the UI:

1. On a Teams or Enterprise plan, open **Dashboard > Plugins > Team Marketplaces > Add Marketplace** and choose **Import from Repo**.
2. Enter `https://github.com/justinyoo/skills`, review **justinyoo-skills**, and configure marketplace access. Enterprise may require an administrator.
3. In Cursor, open **Customize**, find the collection in the team marketplace, and select **Install**.

For local use without a team marketplace, place the repository's plugin files under `<home>/.cursor/plugins/local/justinyoo-skills/`, keeping `plugin.json` and `skills/` at that directory's root. Restart Cursor or run **Developer: Reload Window**, then inspect **Customize**. This requires local plugin imports to be allowed by your organization. The skills CLI is another option when local or team plugins are unavailable.

See [Cursor's plugin and marketplace guide](https://cursor.com/docs/plugins).

### Gemini CLI

Gemini packages the collection as an extension using [gemini-extension.json](../gemini-extension.json). From a terminal, with Git available:

```sh
gemini extensions install https://github.com/justinyoo/skills
```

Restart Gemini CLI after installation, then use `/extensions list` in the interactive session to inspect **justinyoo-skills**. Extension management commands such as `gemini extensions install` run in the terminal, not inside the interactive session. See [Gemini CLI's extension reference](https://geminicli.com/docs/extensions/reference/).

### Trying native plugins from a local checkout

For Copilot CLI, Claude Code, and Codex, replace `justinyoo/skills` with `.` in their **marketplace add** command while working at this repository's root, then install through the same marketplace flow. For Gemini, use `gemini extensions install .`. Cursor's local-plugin directory flow is described above.
