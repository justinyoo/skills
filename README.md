# Skills for AI Coding Agents

A curated collection of **skills** for AI coding agents. A skill packages domain-specific knowledge and, optionally, runnable scripts that an agent can read and execute to perform a well-defined task — for example, removing speaker notes from a PowerPoint file.

Agents discover a skill by reading its `SKILL.md`, then follow the instructions and invoke the bundled scripts as needed.

> [!NOTE]
> This repository primarily focuses on [GitHub Copilot](https://docs.github.com/copilot). If you want to apply the skills to [Claud Code](https://docs.anthropic.com/docs/claude-code), follow the [Using with Claude Code](#using-with-claude-code) section.

## Repository structure

```text
.
├── AGENTS.md             # Guidance for AI coding agents working in this repository
├── scripts/              # Helper scripts (e.g. sync skills to .claude)
│   ├── sync-skills.sh
│   └── sync-skills.ps1
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

## Available skills

| Skill | Description |
| ----- | ----------- |
| [`pptx-denote`](.github/skills/pptx-denote/SKILL.md) | Remove all slide notes from a PowerPoint presentation using the `python-pptx` library. |

## Using a skill

1. Open the skill's `SKILL.md` and read the **How it works** section.
1. Run a prompt with the slash (`/`) command.

   For example, to remove notes from a PowerPoint file, run the prompt like:

    ```
    /pptx-denote <my-pptx-file-to-remove-notes>.pptx
    ```

## Using with Claude Code

Skills in this repository live under `.github/skills/`, which is the location used by
GitHub Copilot and VS Code. [Claude Code](https://docs.anthropic.com/docs/claude-code)
discovers skills from `.claude/skills/` instead, so the skills need to be copied there.

The `SKILL.md` format is the same for both tools, so a copy is all that's required. Use the
bundled sync scripts to copy every skill into `.claude/skills/` (skills that already exist are
left untouched):

```bash
# zsh/bash
./scripts/sync-skills.sh
```

```powershell
# PowerShell
./scripts/sync-skills.ps1
```

After syncing, Claude Code loads each skill's `name` and `description`, then reads the full
`SKILL.md` when a task matches. The `.claude/` directory is ignored by Git, so the synced
copies stay local to your machine.

## Adding a new skill

1. Create `.github/skills/<skill-name>/`.
2. Add a `SKILL.md` with valid YAML frontmatter (`name`, `description`).
3. Place any executable code under `scripts/` and document the exact invocation in `SKILL.md`.
4. List prerequisites (libraries, tools) and how to install them.
5. Keep the skill self-contained, single-purpose, and idempotent where possible.

See [AGENTS.md](AGENTS.md) for the full set of conventions.

## Contributing

Contributions of new skills are welcome. Follow the conventions in [AGENTS.md](AGENTS.md) and
keep each skill focused on a single, well-defined task.
