# Repository maintenance

The canonical content is in `skills/`. This repository stores its authored
skills, thumbnails, documentation, distribution manifests, and lightweight
repository-specific checks. It does not vendor a repository generator,
managed-state framework, or `create-skill` installation.

## Adding or updating skills

Follow [AGENTS.md](../AGENTS.md). When adding, renaming, or removing a skill,
update its entry in [README.md](../README.md) and
[marketplace.json](../marketplace.json), and the skill keywords in
[plugin.json](../plugin.json). The other agent manifests point to the complete
collection and canonical `skills/` directory.

For individual Copilot plugin installation, each skill has a `plugin.json`
inside its directory. Keep its name and version consistent with the marketplace
entry, and set `"skills": "./"` to expose the existing root `SKILL.md` without
duplicating the skill's content.

Authoring helpers are optional external tools. Use an installation already
available to your agent. If `create-skill` is unavailable and needed, obtain
approval before installing it on demand, for example:

```sh
npx skills add jongio/skills --skill create-skill -g --agent github-copilot
```

Follow that tool's preview and approval workflow, preserve this repository's
custom content, and review its proposed registration changes. Do not copy the
helper into `skills/` or introduce managed-state files merely to use it.

## GitHub Actions

The skill-lint workflow installs Vally from the pinned package manifest and
lockfile under `.github/tools/vally/` into the runner's temporary directory.
No validation runtime is committed to the repository. The workflow checks
distribution manifests, skill specifications, and file references.

`.github/scripts/lint-skills.mjs` contains only repository-specific validation
policy. It uses Vally's installed public API; it does not bundle Vally, generate
repository files, or keep ownership hashes.

The existing PRD/TRD/TDD handoff links are explicitly listed in
`.github/tools/vally/allowed-skill-links.json`. Vally's default reference grader
rejects all sibling-skill links, so the wrapper permits those exact links only
when they resolve to existing canonical `SKILL.md` files. Missing targets,
symlinks, undeclared sibling references, and other specification failures still
fail.

Dependency manifests, lockfiles, and policy stay in Git to make CI repeatable.
Dependabot updates the validation dependencies and covers authored skills only
when they have an actual npm package. Documentation-only and Python-only
skills do not need dummy packages.

## Optional local validation

From the repository root with Node.js 24 or newer:

```sh
npm ci --prefix .github/tools/vally --ignore-scripts
node --test test/*.test.mjs
node .github/scripts/lint-skills.mjs skills
```

The local dependency directory is ignored by Git. To use a separate tool
installation, set `SKILLS_VALIDATION_DIR` to a directory containing the pinned
package manifest and its installed dependencies. GitHub Actions sets this to
its temporary installation automatically.

CI runs static checks, not model-based evaluations or authoring agents. It
does not commit, push, publish GitHub Pages, or regenerate repository content.
