# PRD readiness checklist

Assess the content and intended use, not the number of headings, pages, answers, or completed template fields. Unknowns are acceptable in a draft but must not be disguised as facts or silently omitted.

## Content checks

- The problem, primary user, current experience, and intended outcome are clear.
- Evidence and consequential decisions have traceable sources. Hypotheses, proposals, and inaccessible information are labeled honestly.
- Goals describe outcomes. Metrics identify measurement methods, baselines, targets, and evaluation windows where known; missing values are explicit.
- Scope and priorities are understandable. Non-goals, release exclusions, and deferred possibilities are not conflated.
- Essential journeys describe observable behavior, including relevant alternate, failure, empty, boundary, and unauthorized cases.
- In-scope requirements have stable IDs, rationale, priority or release scope, and testable acceptance criteria, or explicit gaps where these are unresolved.
- Applicable quality requirements are specific enough to assess. Terms such as "fast", "scalable", "intuitive", and "secure" do not stand in for criteria.
- Conditional modules were considered proportionately. Unknown applicability was not treated as an exclusion; consequential exclusions have a reason.
- Success metrics, requirement acceptance criteria, and release criteria are distinct and consistent.
- Assumptions, dependencies, risks, and open questions include their impact and known next action or owner. Unknown assignments remain explicit.
- Product constraints are preserved; unnecessary implementation prescriptions and raw interview history are excluded or linked elsewhere.
- The PRD is internally consistent, with no unresolved contradiction hidden by a confident summary or silently changed scope.
- No instructional placeholders or unused example rows remain. A meaningful entry such as "Unknown: retention period; blocks data lifecycle design" is different from an unexplained template token.

## Document status

| Status               | Conditions |
| -------------------- | ---------- |
| Draft                | A useful initial account exists, but foundational information, requirement detail, or consequential decisions remain incomplete or unconfirmed. This is the default. |
| Review-ready         | Problem, users, outcomes, release boundaries, and the essential requirements with observable acceptance criteria are coherent enough for meaningful review. Remaining proposals, risks, and open questions are explicit, and implementation blockers are prominently identified. This does not mean approval. |
| Implementation-ready | Review-ready conditions are met; the user or identified decision-maker has explicitly confirmed the current scope and essential requirements; applicable acceptance, quality, and release criteria are sufficiently defined; and no unresolved question or assumption blocks implementation of the stated scope. Nonblocking unknowns remain visible with known next actions or an explicit deferral. |

Use the highest status whose conditions are fully supported; otherwise retain `Draft`. If the intended use or requested readiness is unclear and affects the interview, ask. Do not force an exploratory PRD to reach implementation-ready.

A blocking unknown is one whose resolution could materially change agreed scope, required behavior, permissions, data handling, safety, or acceptance. A request to "finish now" permits delivering a draft, not inventing a resolution. Unknown owners or missing evidence should not be assigned harmlessness without a basis.

`Implementation-ready` describes the document's suitability for starting work. It does not assert that the product has passed testing, compliance review, or release criteria. Do not use `Approved` or claim stakeholder sign-off without explicit evidence of that approval.

## Final pass

1. Compare the latest user decisions with the draft and update all affected sections, preserving stable requirement IDs.
2. Perform the [reviewer pass](../SKILL.md#6-review-and-cross-check) against the source context and checklist. Correct supported drafting errors and record unresolved findings with affected sections or requirement IDs and their impact. Do not treat reviewer feedback as approval.
3. Resolve the most important gap through a focused question, or record it if deferred. Recheck affected areas after corrections. Do not ask further
   questions after an explicit pause or stop.
4. Assign the supported status and make material blockers easy to find.
5. Save the current draft at the authorized path without overwriting unrelated content. If saving is unavailable, return the Markdown and disclose that.
6. State the location, status, and material unresolved blockers without claiming approval or completeness beyond what the conversation supports.
