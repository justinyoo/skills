/** Static Vally specification checks plus declared, repository-scoped skill links. */
import { lstat, readFile, readdir } from "node:fs/promises";
import { createRequire } from "node:module";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

function relativePath(value) {
  if (
    !value || path.isAbsolute(value) || /[\\:\u0000]/.test(value)
    || value.split("/").some(part => !part || part === ".." || part === "." || part === ".git")
  ) throw new Error(`Unsafe repository reference: ${value}`);
  return value;
}

async function inspect(root, relative) {
  relativePath(relative);
  const parts = relative.split("/");
  let current = root;
  const rootInfo = await lstat(root);
  if (!rootInfo.isDirectory() || rootInfo.isSymbolicLink()) {
    throw new Error("Lint requires a non-symlink repository root.");
  }
  for (let index = 0; index < parts.length; index += 1) {
    current = path.join(current, parts[index]);
    let info;
    try {
      info = await lstat(current);
    } catch (error) {
      if (error.code === "ENOENT") return { kind: "missing" };
      throw error;
    }
    if (info.isSymbolicLink()) return { kind: "symlink" };
    if (index < parts.length - 1 && !info.isDirectory()) return { kind: "non-directory-parent" };
    if (index === parts.length - 1) {
      return { kind: info.isFile() ? "file" : info.isDirectory() ? "directory" : "non-file" };
    }
  }
  throw new Error(`Cannot inspect ${relative}`);
}

async function assertSafeTree(root, relative) {
  if ((await inspect(root, relative)).kind !== "directory") {
    throw new Error(`Missing or unsafe skill directory: ${relative}`);
  }
  for (const entry of await readdir(path.join(root, relative), { withFileTypes: true })) {
    if (entry.isSymbolicLink()) throw new Error(`Symlink in skill sources: ${relative}/${entry.name}`);
    if (["node_modules", ".git", "dist", "build", "vally-results", "__pycache__"].includes(entry.name)) continue;
    if (entry.isDirectory()) await assertSafeTree(root, `${relative}/${entry.name}`);
  }
}

export function validateLinkPolicy(value) {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    throw new Error("Skill-link policy must be an object.");
  }
  for (const [name, links] of Object.entries(value)) {
    if (
      !/^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$/.test(name)
      || !Array.isArray(links)
      || !links.every(link => typeof link === "string" && /^\.\.\/[a-z][a-z0-9-]*\/SKILL\.md$/.test(link))
    ) throw new Error(`Invalid skill-link policy for ${name}`);
  }
  return value;
}

export async function referenceFailures(root, skill, policy) {
  const source = path.relative(root, skill.path).split(path.sep).join("/");
  if (source !== `skills/${skill.name}/SKILL.md` || (await inspect(root, source)).kind !== "file") {
    throw new Error("Lint input must be a canonical, non-symlink skill.");
  }
  const directory = path.dirname(skill.path);
  const declared = Object.hasOwn(policy, skill.name) ? policy[skill.name] : [];
  const failures = [];
  for (const ref of skill.fileReferences) {
    const target = path.resolve(directory, ref.normalized);
    const withinSkill = target === directory || target.startsWith(`${directory}${path.sep}`);
    if (
      path.isAbsolute(ref.normalized) || /^[A-Za-z]:|^\\\\/.test(ref.normalized)
      || (!withinSkill && !declared.includes(ref.normalized))
    ) {
      failures.push(`${ref.normalized}: undeclared or absolute reference`);
      continue;
    }
    const relative = path.relative(root, target).split(path.sep).join("/");
    relativePath(relative);
    const current = await inspect(root, relative);
    const allowedKind = withinSkill
      ? ["file", "directory"].includes(current.kind)
      : current.kind === "file" && /^skills\/[a-z][a-z0-9-]*\/SKILL\.md$/.test(relative);
    if (!allowedKind) failures.push(`${ref.normalized}: ${current.kind}`);
  }
  return failures;
}

export async function lint(rootInput, target = "skills") {
  const root = path.resolve(rootInput);
  const scanRoot = path.resolve(root, target);
  const relative = path.relative(root, scanRoot).split(path.sep).join("/");
  if (relative !== "skills" && !/^skills\/[a-z][a-z0-9-]*$/.test(relative)) {
    throw new Error("Lint only accepts the canonical skills directory or one skill directory.");
  }
  await assertSafeTree(root, relative);
  const toolsDirectory = process.env.SKILLS_VALIDATION_DIR
    ? path.resolve(process.env.SKILLS_VALIDATION_DIR)
    : path.join(root, ".github", "tools", "vally");
  const require = createRequire(path.join(toolsDirectory, "package.json"));
  const { runLint } = await import(pathToFileURL(require.resolve("@microsoft/vally")).href);
  const policy = validateLinkPolicy(JSON.parse(await readFile(
    path.join(root, ".github", "tools", "vally", "allowed-skill-links.json"), "utf8",
  )));
  const result = await runLint({ rootPath: scanRoot });
  const failures = [...result.discoveryErrors];
  if (!result.skillResults.length) failures.push("No skills were found.");
  for (const entry of result.skillResults) {
    const invalid = await referenceFailures(root, entry.skill, policy);
    const otherFailures = entry.graderResults.filter(grader => grader.name !== "valid-refs" && !grader.passed);
    if (invalid.length || otherFailures.length) {
      failures.push({ skill: entry.skill.name, references: invalid, graders: otherFailures });
      console.error(`FAIL ${entry.skill.name}: ${invalid.join("; ")} ${otherFailures.map(item => item.evidence).join("; ")}`);
    } else {
      console.log(`PASS ${entry.skill.name}: specification and repository reference policy`);
    }
  }
  return { passed: failures.length === 0, failures };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  if (process.argv.length > 3) {
    console.error("Usage: node .github/scripts/lint-skills.mjs [skills|skills/<name>]");
    process.exitCode = 1;
  } else {
    lint(process.cwd(), process.argv[2]).then(result => {
      if (!result.passed) {
        console.error(JSON.stringify(result.failures, null, 2));
        process.exitCode = 1;
      }
    }).catch(error => {
      console.error(error.message);
      process.exitCode = 1;
    });
  }
}
