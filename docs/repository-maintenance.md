# Repository maintenance

The canonical content is in `skills/`. This repository stores its authored skills, thumbnails, documentation, distribution manifests, and lightweight repository-specific checks. It does not vendor a repository generator, managed-state framework, or `create-skill` installation.

For installation methods and agent-specific behavior, use the [Skills installation guide](skills-installation-guide.md). This document covers authoring maintenance, registration, and validation.

## Authoring workflow

Prefer the external `create-skill` assisted workflow documented in [README](../README.md#adding-a-new-skill). Reuse an available installation or obtain approval to install it on demand, then review its dry-run before approving the intended changes. Manual authoring remains the fallback.

Both methods follow [AGENTS.md](../AGENTS.md) and the checklist below. Preserve existing custom content and review the helper's registration changes rather than assuming it maintains every repository surface. Do not copy the helper into `skills/`, add authoring to CI, or introduce managed-state files.

## Skill-change checklist

When adding, renaming, updating, or removing a skill, reconcile the applicable entries together:

| File or area                                        | Required consistency                                                                                                                                    |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `skills/<skill-name>/SKILL.md`                      | Keep the frontmatter `name` equal to the directory name, provide a description, and document behavior and runtime prerequisites.                        |
| `skills/<skill-name>/plugin.json`                   | Use the same name, a version matching the individual marketplace entry, and `"skills": "./"` to expose the root `SKILL.md`.                             |
| [marketplace.json](../marketplace.json)             | Maintain the individual plugin entry and its `./skills/<skill-name>` source. Preserve the separate collection plugin entry.                             |
| [README.md](../README.md#available-skills)          | Keep the available-skills table and its links current.                                                                                                  |
| Collection [plugin.json](../plugin.json)            | Keep skill keywords consistent with the authored collection. Do not confuse this manifest with each skill's own `plugin.json`.                          |
| [.github/dependabot.yml](../.github/dependabot.yml) | Add or remove an npm entry only when the skill has an actual `package.json`; do not create dummy packages for documentation-only or Python-only skills. |
| Supporting files                                    | Keep scripts, references, locale rules, and any thumbnail files consistent with the skill. Preserve unrelated authored content.                         |

The other host manifests expose the complete collection through the canonical `skills/` directory. Reconcile them when collection identity, version, or layout changes; they do not need an individual entry for every new skill.

## GitHub Actions

The [skill-lint workflow](../.github/workflows/skill-lint.yml) installs Vally from the pinned package manifest and lockfile under `.github/tools/vally/` into `$RUNNER_TEMP/skills-validation`. The installation step exports `SKILLS_VALIDATION_DIR` through `$GITHUB_ENV` for later steps. No validation runtime is committed to the repository.

CI runs repository tests, static skill specification/reference checks, deterministic npm tests for skills with `package.json`, and static lint for any eval specifications. Keep skill-level `npm test` commands deterministic; model-based evaluations are separate, explicitly authorized work.

`.github/scripts/lint-skills.mjs` contains only repository-specific validation policy. It uses Vally's installed public API; it does not bundle Vally, generate repository files, or keep ownership hashes.

The existing PRD/TRD/TDD handoff links are explicitly listed in `.github/tools/vally/allowed-skill-links.json`. Vally's default reference grader rejects all sibling-skill links, so the wrapper permits those exact links only when they resolve to existing canonical `SKILL.md` files. Missing targets, symlinks, undeclared sibling references, and other specification failures still fail.

Dependency manifests, lockfiles, and policy stay in Git to make CI repeatable. Dependabot updates the validation dependencies and covers authored skills only when they have an actual npm package. Documentation-only and Python-only skills do not need dummy packages.

## Local validation

From the repository root with Node.js 24 or newer:

### Repository tests

The repository tests use Node's built-in test runner and require no dependency installation:

```sh
node --test
```

There is no root `package.json`, so do not run a bare `npm test` at the root.

### Static skill linting

Install the pinned validation dependencies only when you want to run static skill linting locally:

```sh
npm ci --prefix .github/tools/vally --ignore-scripts
node .github/scripts/lint-skills.mjs skills
```

The local dependency directory is ignored by Git. To use a separate tool installation, set `SKILLS_VALIDATION_DIR` to a directory containing the pinned package manifest and its installed dependencies. GitHub Actions sets this to its temporary installation automatically.

Running a skill still requires its own prerequisites from `SKILL.md`; the Vally toolchain does not install them.

CI does not run model-based evaluations or authoring agents, commit, push, publish GitHub Pages, or regenerate repository content.
