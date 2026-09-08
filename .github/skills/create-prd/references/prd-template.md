# PRD template

Use the outline below as a starting point, not a form to fill mechanically. Replace instructional placeholders with sourced content, a clearly labeled proposal, or an explicit unknown. Remove unused example rows and optional subsections rather than leaving decorative empty tables.

Keep the core information covered even when combining headings. Add conditional modules from the interview guide only where relevant. A small feature may need only a few paragraphs and a short requirements list.

```markdown
# [Product or feature] - Product requirements document

| Field                     | Value                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------ |
| Version                   | [Document version, distinct from the product release; confirmed or proposed]         |
| Status                    | Draft / Review-ready / Implementation-ready                                          |
| Owner                     | [Known owner, or unknown]                                                            |
| Collaborators / reviewers | [Known participants, or unknown]                                                     |
| Last updated              | [Actual update date]                                                                 |
| Sign-off date             | [Actual sign-off date for this version with explicit approval, or pending / unknown] |
| Intended audience         | [Who will use this PRD and for what decision]                                        |
| Release scope             | [Named release or scope, if known]                                                   |
| Target release            | [Confirmed constraint, proposed date, or unknown; not an invented commitment]        |

## 1. Overview

[Briefly describe the product or change, intended user benefit, and proposed solution direction. Identify whether the solution direction is confirmed or proposed.]

## 2. Problem and evidence

- Problem: [What is difficult or impossible today.]
- Current experience: [Existing workflow or workaround and its shortcomings.]
- Evidence: [Research, observations, or user-provided claims with source links.]
- Why now: [Relevant urgency or business context, when known.]
- Hypotheses: [Beliefs not yet supported by evidence.]

## 3. Users and key journeys

[Identify the primary user, their need, and relevant secondary actors.]

### Primary journey

[Describe the trigger, key interactions, and desired result. Include important alternate or failure paths. Link to designs when available; capture required interaction behavior here without reproducing exhaustive visual specifications.]

## 4. Goals and success measures

| Goal ID | Desired outcome | Metric and measurement method                | Baseline           | Target                            | Evaluation window  |
| ------- | --------------- | -------------------------------------------- | ------------------ | --------------------------------- | ------------------ |
| G-001   | [Outcome]       | [Observable measure and how it is collected] | [Known or unknown] | [Confirmed, proposed, or unknown] | [Known or unknown] |

[Include guardrail metrics when relevant. Metrics evaluate product impact, not merely whether a feature was implemented. Identify who evaluates them if known.]

## 5. Scope and priorities

### In scope

[Capabilities needed for this release, with a consistent, explained priority scheme. Do not classify everything as essential without a rationale.]

### Non-goals

[Outcomes deliberately not pursued.]

### Out of scope for this release

[Capabilities explicitly excluded from the current scope.]

### Deferred ideas

[Optional: possible future work, explicitly not a roadmap commitment.]

## 6. Functional requirements

### FR-001: [Short, behavior-oriented title]

- State and source: [Confirmed or proposed; source or user decision.]
- User need / rationale: [Why this behavior is necessary; related goal or journey.]
- Priority / release scope: [Agreed priority, or explicitly proposed.]
- Actor and trigger: [Who initiates the behavior and under what conditions.]
- Required behavior: [One clear, externally observable behavior.]
- Rules and boundaries: [Permissions, limits, state changes, and exceptions as relevant.]
- Acceptance criteria:
  - [Observable condition that demonstrates the requirement is satisfied.]
  - [Relevant failure, empty, boundary, or unauthorized case.]
- Dependencies / open questions: [Related requirement IDs, source links, or unresolved decisions.]

[Repeat the record for each requirement. Preserve IDs when revising; do not renumber existing requirements merely to match display order.]

## 7. Quality requirements and constraints

| ID      | Area                    | Requirement or constraint             | Acceptance measure                           | State / source                               |
| ------- | ----------------------- | ------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| NFR-001 | [Relevant quality area] | [Specific required behavior or bound] | [Observable measure under stated conditions] | [Confirmed / proposed / unknown, with basis] |

[Consider performance, reliability, accessibility, security, privacy, compatibility, and compliance proportionately. Record why consequential areas are not applicable. Avoid unqualified terms such as "fast" or "secure".]

[Capture actual business or technical constraints and required integration behavior. Link to detailed implementation decisions rather than inventing them.]

## 8. Release and evaluation

- Release criteria: [Conditions required before exposing the capability to users.]
- Rollout: [Audience, stages, or enablement conditions where relevant.]
- Recovery / rollback: [Required behavior or conditions where relevant.]
- Timing and dependencies: [Known constraints and high-level milestones only.]
- Post-launch evaluation: [When and by whom outcomes and guardrails are reviewed, if known.]

[Release criteria are distinct from acceptance criteria and success metrics. Document readiness is not evidence that the product itself is ready to ship.]

## 9. Risks and unresolved decisions

### Assumptions

| ID    | Assumption                      | Impact if wrong | Validation or next action | Owner                    |
| ----- | ------------------------------- | --------------- | ------------------------- | ------------------------ |
| A-001 | [Explicitly unvalidated belief] | [Impact]        | [Known action or unknown] | [Known owner or unknown] |

### Risks and dependencies

| ID     | Risk or dependency   | Impact   | Mitigation or next action   | Owner                    |
| ------ | -------------------- | -------- | --------------------------- | ------------------------ |
| RD-001 | [Risk or dependency] | [Impact] | [Agreed or proposed action] | [Known owner or unknown] |

### Open questions

| ID    | Question or conflict  | Affected goal / requirement | Blocks implementation?  | Owner / next action                  |
| ----- | --------------------- | --------------------------- | ----------------------- | ------------------------------------ |
| Q-001 | [Unresolved decision] | [Related IDs or area]       | [Yes / no, with reason] | [Known owner and action, or unknown] |

### Decisions and material changes

| Date          | Decision or change                               | Basis / confirmed by              | Affected scope or IDs |
| ------------- | ------------------------------------------------ | --------------------------------- | --------------------- |
| [Actual date] | [Decision, or change from the previous baseline] | [Source or explicit confirmation] | [Affected areas]      |

### Supporting references

[List the source documents and linked design, technical, research, or delivery artifacts actually used. Do not invent links or imply inaccessible sources were read.]
```
