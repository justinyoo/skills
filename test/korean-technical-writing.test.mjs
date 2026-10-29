import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const skill = new URL("../skills/korean-technical-writing/", import.meta.url);
const parse = async relative => JSON.parse(await readFile(new URL(relative, skill), "utf8"));

test("Korean writing pilot fixtures identify the skill and remain explicitly unexecuted", async () => {
  const [fixtures, plugin] = await Promise.all([
    parse("evals/evals.json"),
    parse("plugin.json"),
  ]);
  assert.equal(fixtures.skill_name, plugin.name);
  assert.equal(fixtures.evaluation_status, "not_run");
  assert.equal(typeof fixtures.description, "string");
  assert.match(fixtures.description, /\S/);
});

test("the six Korean writing pilot cases have unique IDs and complete grading inputs", async () => {
  const fixtures = await parse("evals/evals.json");
  assert.ok(Array.isArray(fixtures.evals));
  assert.equal(fixtures.evals.length, 6);
  const ids = new Set();
  for (const entry of fixtures.evals) {
    assert.ok(entry && typeof entry === "object" && !Array.isArray(entry));
    assert.ok(Number.isSafeInteger(entry.id) && entry.id > 0);
    assert.equal(ids.has(entry.id), false, `Duplicate case ID: ${entry.id}`);
    ids.add(entry.id);
    for (const field of ["prompt", "expected_output"]) {
      assert.equal(typeof entry[field], "string", `Case ${entry.id}: ${field}`);
      assert.match(entry[field], /\S/, `Case ${entry.id}: empty ${field}`);
    }
    assert.ok(Array.isArray(entry.assertions) && entry.assertions.length > 0);
    for (const assertion of entry.assertions) {
      assert.equal(typeof assertion, "string", `Case ${entry.id}: assertion`);
      assert.match(assertion, /\S/, `Case ${entry.id}: empty assertion`);
    }
  }
});
