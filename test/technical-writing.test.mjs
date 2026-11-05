import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import test from "node:test";

const skill = new URL("../skills/technical-writing/", import.meta.url);
const read = relative => readFile(new URL(relative, skill), "utf8");
const parse = async relative => JSON.parse(await read(relative));

test("English writing metadata matches the individual plugin", async () => {
  const [instructions, plugin] = await Promise.all([
    read("SKILL.md"),
    parse("plugin.json"),
  ]);
  const frontmatter = instructions.match(/^---\n([\s\S]*?)\n---/);
  assert.ok(frontmatter);
  assert.match(frontmatter[1], /^name: technical-writing$/m);
  assert.match(frontmatter[1], /English technical and general writing/);
  assert.match(frontmatter[1], /non-English output/);
  const version = frontmatter[1].match(/^  version: "([^"]+)"$/m);
  assert.ok(version);
  assert.equal(version[1], plugin.version);
  assert.equal(plugin.name, "technical-writing");
  assert.equal(plugin.skills, "./");
});

test("the README uses the skill's installation and invocation commands", async () => {
  const readme = await read("README.md");
  assert.match(readme, /copilot plugin marketplace add justinyoo\/skills/);
  assert.match(readme, /copilot plugin install technical-writing@justinyoo-skills/);
  assert.match(readme, /^\/technical-writing /m);
});

test("relative links in the skill documents resolve", async () => {
  for (const relative of ["SKILL.md", "README.md", "references/sources.md"]) {
    const source = new URL(relative, skill);
    const text = await read(relative);
    const links = [...text.matchAll(/\]\(([^)]+)\)/g)];
    assert.ok(links.length > 0, `No links found in ${relative}`);
    for (const [, href] of links) {
      const target = new URL(href, source);
      if (target.protocol !== "file:") continue;
      target.hash = "";
      target.search = "";
      await assert.doesNotReject(access(target), `${relative}: ${href}`);
    }
  }
});

test("the source register includes contextual references without making them universal rules", async () => {
  const [instructions, sources, readme] = await Promise.all([
    read("SKILL.md"),
    read("references/sources.md"),
    read("README.md"),
  ]);
  for (const reference of [
    "Merriam-Webster Dictionary",
    "Oxford English Dictionary",
    "US Federal Plain Language Guidelines",
    "GOV.UK Style Guide",
    "Australian Style Manual",
    "The Chicago Manual of Style",
    "AP Stylebook",
    "APA Style",
    "MLA Style Center",
  ]) {
    assert.ok(sources.includes(reference), `Missing reference: ${reference}`);
  }
  assert.match(sources, /universal grammar rule/i);
  assert.match(instructions, /not interchangeable or universal rules/i);
  assert.match(readme, /not universal rules/i);
});

test("English writing evaluation cases are explicitly unrun", async () => {
  const [fixtures, plugin] = await Promise.all([
    parse("evals/evals.json"),
    parse("plugin.json"),
  ]);
  assert.equal(fixtures.skill_name, plugin.name);
  assert.equal(fixtures.evaluation_status, "not_run");
  assert.equal(typeof fixtures.description, "string");
  assert.match(fixtures.description, /\S/);
});

test("English writing evaluation cases have unique identifiers and complete inputs", async () => {
  const fixtures = await parse("evals/evals.json");
  const requiredScenarios = [
    "preserve-observed-measurements",
    "preserve-obligations-and-conditions",
    "minimal-proofreading-existing-variant",
    "new-document-us-default",
    "technical-procedure-safety",
    "protect-literal-text-and-punctuation",
    "review-only-conflict",
    "general-email-no-invention",
    "no-standards-certification",
    "ask-about-ambiguous-referent",
    "house-style-for-new-document",
    "preserve-uncertainty",
    "preserve-range-boundaries",
    "save-needs-destination",
  ];
  assert.ok(Array.isArray(fixtures.evals));
  const ids = new Set();
  const scenarios = new Set();
  for (const entry of fixtures.evals) {
    assert.ok(entry && typeof entry === "object" && !Array.isArray(entry));
    assert.ok(Number.isSafeInteger(entry.id) && entry.id > 0);
    assert.equal(ids.has(entry.id), false, `Duplicate case ID: ${entry.id}`);
    ids.add(entry.id);
    for (const field of ["scenario", "prompt", "expected_output"]) {
      assert.equal(typeof entry[field], "string", `Case ${entry.id}: ${field}`);
      assert.match(entry[field], /\S/, `Case ${entry.id}: empty ${field}`);
    }
    assert.equal(scenarios.has(entry.scenario), false, `Duplicate scenario: ${entry.scenario}`);
    scenarios.add(entry.scenario);
    assert.ok(Array.isArray(entry.assertions) && entry.assertions.length > 0);
    for (const assertion of entry.assertions) {
      assert.equal(typeof assertion, "string", `Case ${entry.id}: assertion`);
      assert.match(assertion, /\S/, `Case ${entry.id}: empty assertion`);
    }
  }
  for (const scenario of requiredScenarios) {
    assert.ok(scenarios.has(scenario), `Missing scenario: ${scenario}`);
  }
});
