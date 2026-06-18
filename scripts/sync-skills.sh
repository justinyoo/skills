#!/usr/bin/env bash
#
# sync-skills.sh
#
# Copy every skill under .github/skills to .claude/skills.
# Skills that already exist in the destination are left untouched.
#
# Usage:
#   ./scripts/sync-skills.sh
#
set -euo pipefail

# Resolve the repository root (the parent of this script's directory).
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/.." && pwd)"

src_dir="${repo_root}/.github/skills"
dest_dir="${repo_root}/.claude/skills"

if [[ ! -d "${src_dir}" ]]; then
  echo "Error: source directory not found: ${src_dir}" >&2
  exit 1
fi

mkdir -p "${dest_dir}"

copied=0
skipped=0

for skill_path in "${src_dir}"/*/; do
  # Skip if the glob did not match any directory.
  [[ -d "${skill_path}" ]] || continue

  skill_name="$(basename "${skill_path}")"
  target="${dest_dir}/${skill_name}"

  if [[ -e "${target}" ]]; then
    echo "Skipping '${skill_name}' (already exists)."
    skipped=$((skipped + 1))
    continue
  fi

  cp -R "${skill_path%/}" "${target}"
  echo "Copied '${skill_name}'."
  copied=$((copied + 1))
done

echo "Done. Copied ${copied} skill(s), skipped ${skipped}."
