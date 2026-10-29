# Korean Technical Writing

English | [한국어](README.ko.md)

## What this skill is for

Draft, proofread, revise, or review Korean technical writing while preserving meaning, facts, terminology, and protected expressions. The same Korean foundation also applies to emails, notices, proposals, and essays without forcing them into a technical-manual format. No runtime scripts, packages, or correction service are required. Files change only when explicitly requested; review-only requests leave the original unchanged.

Neither ASD-STE100 nor ISO 24495-1 alone covers this skill's Korean-writing scope. STE is an English controlled language whose rules and dictionary cannot simply be transferred to Korean. ISO's reader-centered plain-language principles do not themselves determine Korean spelling, spacing, natural expression, or technical truth. The skill therefore supplements those principles with National Institute of Korean Language (국립국어원) resources for Korean orthography, particles and dependent nouns, auxiliary verbs, technical terms, punctuation, and permitted variants.

See the [source comparison](references/sources.md#comparison) for their complementary roles and limits, and [SKILL.md](SKILL.md) for the authoritative workflow. The [source usage and rights notes](references/sources.md#source-usage-and-rights) distinguish ASD, ISO, and Korean resource conditions from the MIT license on this skill's original content. External standards and dictionaries are not bundled, and no institutional approval or conformity certification is claimed.

## Install with GitHub Copilot CLI

With GitHub Copilot CLI installed, run these commands in your terminal:

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install korean-technical-writing@justinyoo-skills
```

If you already registered the marketplace, skip the first command. If you installed the complete collection, this skill is already included.

For other agents, installation methods, and local checkouts, see the [Skills installation guide](../../docs/skills-installation-guide.md).

## Usage

In a GitHub Copilot CLI session, try:

```text
/korean-technical-writing 다음 기술 안내문을 윤문해 주세요. 조건과 의무를 유지하고 결과는 대화에만 보여 주세요: "백업이 완료된 경우에만 설정을 변경할수 있습니다. 변경한 뒤에는 서비스를 다시 시작해야 합니다."
```
