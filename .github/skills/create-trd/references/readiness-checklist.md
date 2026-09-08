# TRD readiness checklist

Assess the actual document against its PRD baseline, supplied technical sources, and latest user decisions. Readiness depends on content and intended use, not the number of sections or questions answered.

## Prerequisite and companion checks

- A readable PRD establishes the product foundation for the documented scope. A missing PRD led to a request to generate one first, not a standalone TRD.
- The PRD source, revision/version or explicit unknown, stated status, scope, and consultation date are recorded. Partial or inaccessible context is disclosed.
- Product intent, scope, essential behavior, and product acceptance remain authoritative in the PRD. The TRD provides technical elaboration without duplicating the full product document.
- Product changes discovered in the interview were resolved in the PRD with authorization, or remain explicit blockers. No TRD requirement silently expands scope or weakens PRD acceptance.
- PRD and TRD changes are reconciled; an older TRD does not retain its readiness status automatically after a material baseline change.

## Coverage and requirement checks

- The technical boundary, actors, affected systems, responsibilities, and release exclusions are understandable and consistent with the PRD.
- Actual constraints and dependencies have sources and impact. Existing code, draft architecture, and preferences are not misrepresented as mandates.
- Every interview-guide area was screened proportionately. Applicability is distinct from certainty, consequential exclusions have reasons, and unknown applicability was not silently dropped.
- Conditional modules are expanded only where needed; small projects retain essential coverage without unnecessary chapters.
- Technical requirements have stable IDs, one clear obligation, state and source, rationale, priority/release scope, and testable acceptance criteria or explicit gaps.
- Relevant normal, boundary, invalid, unauthorized, concurrent, duplicate, and failure cases are addressed proportionately.
- Applicable data integrity/lifecycle, interface, security/privacy, quality, operational, recovery, and compatibility obligations are assessable rather than vague aspirations.
- Quantitative criteria specify or reference meaningful measurement conditions. Targets, workloads, windows, environments, and evidence are not invented.
- Each in-scope PRD requirement has technical coverage, an explicit gap, or a justified statement that no additional technical requirement is needed. The latter does not waive the PRD requirement.
- Every TRD requirement traces to the PRD or another authoritative obligation relevant to its scope, and to acceptance/verification expectations.
- Product metrics, technical acceptance, release gates, and document readiness are distinct. Planned evidence is not described as executed or passed.
- Detailed implementation design, alternatives, physical schemas, test scripts/results, task schedules, and runbooks are linked rather than copied, except for actual binding constraints or essential contract details.
- Assumptions, proposals, risks, conflicts, and unknowns are explicit, with affected references, impact, implementation/release blocking status, and known owner or next action.
- There are no unsupported approvals, compliance claims, sensitive examples, invented links, unused example rows, or instructional placeholders. A meaningful unknown is not a placeholder.
- Existing requirement IDs and unrelated content are preserved, and material baseline changes or superseded requirements are recorded.

## Document status

| Status               | Conditions |
| -------------------- | ---------- |
| Draft                | The PRD prerequisite is satisfied and a useful TRD exists, but technical requirements, applicability, verification, source coverage, or consequential decisions remain incomplete or unconfirmed. This is the default. |
| Review-ready         | The PRD baseline, technical scope, essential technical requirements with meaningful acceptance expectations, coverage dispositions, and traceability are coherent enough for review. Proposals and unresolved findings are explicit, and implementation/release blockers are prominent. This is not approval. |
| Implementation-ready | Review-ready conditions are met; the user or identified decision-maker has explicitly confirmed the current product scope and essential requirements in the PRD and the technical obligations in the TRD; relevant acceptance and verification conditions are sufficiently defined; and no unresolved product or technical issue blocks implementation of this scope. Remaining nonblocking issues have known next actions or explicit deferral with a supported reason. |

Use the highest status supported by evidence; otherwise retain `Draft`. Before the PRD prerequisite is met, report generation as blocked rather than creating an empty TRD labeled `Draft`.

A blocking unknown is one whose resolution could materially change scope, required behavior, system boundaries, permissions, data handling, safety, interfaces, or acceptance. Unknown impact cannot simply be labeled nonblocking. A draft or review-ready PRD may support a draft or review-ready TRD; do not require a PRD to contain technical implementation details.

Distinguish implementation blockers from release gates that are expected to be satisfied later, such as producing verification evidence against already-defined criteria. `Implementation-ready` does not mean the implementation has passed tests, operational checks, compliance review, or release gates. Do not claim `Approved` or sign-off without explicit evidence for the applicable document version.

## Final pass

1. Read the latest PRD and TRD, and compare them with supplied sources and confirmed user decisions. Disclose any inaccessible context that limits the comparison.
2. Perform the reviewer pass in the skill workflow. Identify concrete findings with affected references, evidence, impact, blocking status, and a correction or focused question.
3. Correct supported drafting errors. Return unresolved technical decisions to the interview and product decisions to the PRD handoff. Recheck affected requirements, traceability, risks, and status.
4. If evidence or decisions remain unavailable, record the gap instead of inventing a resolution or repeating review without new information. Honor an explicit pause or stop without further questions.
5. Assign the supported status and make material blockers prominent. Reviewer feedback and a clean review do not provide approval.
6. Save the current TRD at the authorized path without overwriting unrelated content. If writing is unavailable, return the Markdown and disclose it is unsaved.
7. State the location, status, PRD baseline, and material unresolved blockers, or the unmet PRD prerequisite when no TRD was started.
