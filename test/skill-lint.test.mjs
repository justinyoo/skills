import assert from "node:assert/strict";
import { mkdtemp, mkdir, rm, symlink, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import { referenceFailures, validateLinkPolicy } from "../.github/scripts/lint-skills.mjs";

async function fixture(t) {
  const root = await mkdtemp(path.join(os.tmpdir(), "skills-link-policy-"));
  t.after(() => rm(root, { recursive: true, force: true }));
  for (const name of ["source", "dependency"]) {
    await mkdir(path.join(root, "skills", name), { recursive: true });
    await writeFile(path.join(root, "skills", name, "SKILL.md"), `# ${name}\n`);
  }
  return {
    root,
    skill: {
      name: "source",
      path: path.join(root, "skills", "source", "SKILL.md"),
      fileReferences: [],
    },
  };
}

test("only explicitly declared sibling SKILL links are accepted", async t => {
  const { root, skill } = await fixture(t);
  skill.fileReferences = [{ normalized: "../dependency/SKILL.md" }];
  assert.equal((await referenceFailures(root, skill, {})).length, 1);
  assert.deepEqual(
    await referenceFailures(root, skill, { source: ["../dependency/SKILL.md"] }),
    [],
  );
});

test("declared links still require an existing target", async t => {
  const { root, skill } = await fixture(t);
  skill.fileReferences = [{ normalized: "../missing/SKILL.md" }];
  const failures = await referenceFailures(root, skill, { source: ["../missing/SKILL.md"] });
  assert.equal(failures.length, 1);
  assert.match(failures[0], /missing/);
});

test("internal references are checked rather than waived", async t => {
  const { root, skill } = await fixture(t);
  skill.fileReferences = [{ normalized: "SKILL.md" }, { normalized: "missing.md" }];
  const failures = await referenceFailures(root, skill, {});
  assert.equal(failures.length, 1);
  assert.match(failures[0], /missing\.md/);
});

test("reference paths cannot traverse a directory symlink", async t => {
  const { root, skill } = await fixture(t);
  await symlink(
    path.join(root, "skills", "dependency"),
    path.join(root, "skills", "source", "linked"),
    process.platform === "win32" ? "junction" : "dir",
  );
  skill.fileReferences = [{ normalized: "linked/SKILL.md" }];
  assert.match((await referenceFailures(root, skill, {}))[0], /symlink/);
});

test("policy cannot permit arbitrary external paths or invalid identities", () => {
  for (const value of [
    null, [], { source: ["../../secret"] }, { source: ["/secret"] },
    { "invalid/name": ["../dependency/SKILL.md"] }, { source: "not-an-array" },
  ]) {
    assert.throws(() => validateLinkPolicy(value), /policy/);
  }
});
