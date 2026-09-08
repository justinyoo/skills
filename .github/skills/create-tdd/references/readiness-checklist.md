# TDD readiness checklist

Assess the actual TDD against the governing PRD, TRD, applicable ADRs, accessible technical evidence, and latest user decisions. Readiness is about an actionable, coherent design for its stated scope, not document length or the number of interview questions.

## Content checks

### Prerequisites and boundaries

- Both a readable PRD and TRD establish a coherent foundation for the same intended scope. Missing documents led to permission-based upstream handoffs, not standalone design or a placeholder TDD.
- Empty templates, inaccessible sources, and foundational scope/behavior/acceptance conflicts were not treated as satisfied prerequisites. Partial context and unknown revisions are disclosed.
- PRD/TRD sources, revisions or explicit unknowns, stated status, and consultation dates are recorded. Existing implementation references are identifiable, or the lack of code/access is stated.
- Product intent and acceptance remain in the PRD; technical obligations and acceptance remain in the TRD; the TDD owns solution mechanisms and design rationale.
- Proposed requirement changes were resolved upstream with authorization and reconciled downstream, or remain explicit blockers. The design does not silently weaken acceptance or expand scope.
- Existing code and conventions are distinguished from requirements, binding constraints, and intended future behavior.

### Design and coverage

- Scope, non-goals, current versus target state, component responsibilities, data ownership, and boundaries are understandable.
- Every interview-guide area was screened proportionately. Applicability and decision certainty are separate, exclusions have reasons, and consequential unknowns are visible.
- The design explains concrete mechanisms and essential flows rather than repeating the requirements or prescribing unnecessary complexity.
- Relevant invalid, unauthorized, duplicate, concurrent, timeout, partial-failure, and recovery paths are addressed.
- Applicable data lifecycle, interface compatibility, security/privacy, performance/capacity, reliability, and operational mechanisms are explicit enough for the intended implementation scope.
- Applicable migration and rollout account for existing data and mixed versions, integrity/reconciliation, rollback mechanisms, and irreversible steps. Rollback is not asserted without a workable design or an explicit limitation.
- New dependencies and abstractions have a requirement-backed rationale; existing capabilities and patterns were considered before replacement.
- Every in-scope TRD obligation, including PRD obligations it retains without a separate technical requirement, has a design mapping, an explicit gap, or a sourced explanation of an unchanged satisfying mechanism. No obligation is waived because no new code or technical elaboration is needed.
- Consequential design elements trace back to requirements or other authoritative constraints relevant to this scope. Stable IDs and upstream references are preserved.
- Applicable quantitative feasibility reasoning uses the TRD's measurement conditions and targets. Assumptions, estimates, untested capabilities, and evidence limitations are explicit.
- The verification strategy references TRD acceptance and identifies relevant methods and required evidence without inventing executed work or results.

### Decisions and ADR awareness

- Significant choices record context, affected requirements, credible alternatives, rationale, consequences, status, and a confirmation basis or explicit pending decision.
- Recommendations, user preferences, accepted decisions, and organizational approval are not conflated.
- Existing ADRs are linked with their actual status and applicable scope. Proposed, deprecated, or superseded records are not treated as current mandates.
- Conflicts with accepted ADRs remain explicit blockers unless resolved by the appropriate authority and recorded consistently with the applicable decision process.
- ADR candidates are flagged only when justified; standalone ADRs are neither required nor automatically generated.
- TDD updates preserve material decision history and do not silently rewrite or supersede accepted ADRs.

### Safety, updates, and document integrity

- Source limitations, assumptions, risks, and open questions identify affected references, impact, implementation/release blocking status, and known owners or next actions.
- Unknown impact is not labeled nonblocking without a supported reason. Agreed deferrals are explicit.
- No secrets, unnecessary personal data, unsupported compliance claims, fabricated evidence/links/approvals, or unused template instructions remain.
- Existing IDs and unrelated content are preserved. Changed or removed requirement sources and superseded design decisions have a recorded disposition; retired IDs are not reused.
- Material upstream changes have been reconciled and readiness reassessed.
- No code implementation, infrastructure changes, dependency installation, experiments, publication, or extra artifact creation occurred without separate authorization.

## Document status

| Status               | Conditions |
| -------------------- | ---------- |
| Draft                | Both prerequisites and a coherent foundation are present, and a useful design exists, but design detail, coverage, feasibility evidence, or consequential decisions remain incomplete or unconfirmed. This is the default. |
| Review-ready         | Baselines and scope are clear; the proposed solution, essential flows, rationale and alternatives where warranted, coverage mapping, and verification approach are coherent enough for review. Assumptions, unresolved findings, and implementation/release blockers are prominent. This is not approval. |
| Implementation-ready | Review-ready conditions are met; the user or identified decision-maker has explicitly confirmed the governing product scope and essential technical obligations, and the appropriate decision-maker has confirmed consequential design choices for this scope. No unresolved requirement, design, ADR conflict, or feasibility issue blocks implementation. Nonblocking issues have known next actions or explicit deferrals with supported reasons. |

Use the highest status supported by evidence; otherwise retain `Draft`. Before the prerequisites are satisfied, report generation as blocked instead of producing an empty document.

A design-critical unknown is one whose resolution could materially change required behavior, architecture, boundaries, data integrity, permissions, safety, compatibility, or feasibility. If a prototype or other evidence is needed to settle such a choice, that missing evidence blocks implementation readiness; planned evidence is not a successful result.

Conversely, implementation-ready does not require running all future implementation tests, producing release evidence, or turning routine coding choices into approval gates. Distinguish design-critical evidence from tests and operational release gates that can only be completed later. Document status is neither approval to start coding nor evidence that the system is ready to ship.

Do not infer approval from silence, a generated document, upstream filenames/status labels, or a reviewer pass with no findings. Record actual confirmation and its scope; do not invent sign-off.

## Final pass

1. Read the latest TDD and governing PRD/TRD, applicable ADRs, and relevant accessible evidence. Disclose any limitations affecting fidelity or feasibility.
2. Perform the structured [reviewer pass](../SKILL.md#7-review-and-reconcile) in the workflow. Record concrete findings with affected references, evidence, impact, blocking status, and a correction or focused question.
3. Correct source-supported drafting errors. Return unresolved design choices to the interview and requirement changes upstream with permission. Recheck affected areas without inventing missing evidence.
4. Assign the supported status, making blockers and deferred issues explicit. Honor a pause or stop without further questions.
5. Save at the authorized path without overwriting unrelated content. If writing is unavailable, return Markdown and disclose that it is unsaved.
6. State the output location, status, PRD/TRD baselines, and material blockers, or the unmet prerequisites when no TDD was started.
