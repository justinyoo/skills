# Adaptive TRD interview guide

This is a coverage screen and question bank, not a fixed questionnaire. Read the PRD and supplied technical context first. Ask one focused question at a time, skip answered questions, and update all affected areas after each material answer.

## Context and prerequisites

### PRD gate and document boundaries

| Situation                                                   | Next action                                                                                                                  |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| No relevant PRD exists                                      | Ask whether to generate the PRD first using `create-prd`. Allow supplying an existing PRD or pausing. Do not start a TRD.    |
| PRD exists but is inaccessible                              | Request an accessible copy or sufficient excerpt; disclose limits rather than reconstructing the PRD.                        |
| Multiple possible PRDs or conflicting baselines             | Ask which source governs the intended release.                                                                               |
| PRD is empty or lacks product foundation                    | Ask to complete the PRD first; do not conduct product discovery inside the TRD.                                              |
| Draft PRD establishes intent, scope, and essential behavior | Draft a TRD with honest uncertainty; do not demand detailed technical design or blanket PRD approval first.                  |
| Technical discovery would change the PRD                    | Ask to resolve the affected product decision in the PRD before adopting the change in the TRD.                               |
| User declines the PRD prerequisite or stops                 | Pause generation, preserve an existing draft without overstating readiness, and state the blocker without further questions. |

Example opening when no PRD exists:

> A TRD defines the technical obligations supporting a PRD; it should not absorb product discovery. Would you like to generate the PRD first?

With a question tool, offer separate choices for generating the PRD with `create-prd`, supplying an existing PRD, or pausing. Do not silently invoke PRD creation.

### Foundation after the PRD gate

Select only consequential unanswered questions:

| Area               | Example next question                                                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Baseline           | Which PRD revision governs this release?                                                                             |
| Intended use       | What decision should this TRD enable the engineering team to make?                                                   |
| Technical boundary | Which system is responsible for completing this operation?                                                           |
| Existing behavior  | Which current integration contract must remain compatible?                                                           |
| Constraint         | Is this platform choice mandated by an existing decision?                                                            |
| Source conflict    | The PRD requires deletion, but the supplied policy requires retention; which authority should resolve this conflict? |

If a version, owner, or decision is unknown, label it rather than repeatedly asking. Escalate only when the uncertainty affects the baseline or intended readiness.

## Choosing the next question

Prioritize the decision with the greatest effect on scope, required behavior, safety, interfaces, data integrity, or acceptance. Resolve contradictions before refining dependent details. Offer choices with tradeoffs where useful, without treating the recommendation as confirmed.

Distinguish these question types:

| Type                  | Example                                                                                    | Where the answer belongs                                              |
| --------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| Product decision      | Must users be able to undo a completed transaction?                                        | PRD first, if not already established                                 |
| Technical requirement | During a retry, how must the system recognize that the same transaction already completed? | TRD, consistent with the product behavior                             |
| Implementation choice | Which internal table stores the deduplication key?                                         | Usually TDD/specification; only a TRD constraint if actually mandated |

Do not open with "Which database/framework/cloud should we use?" unless the context makes it a real constraint. Prefer asking which existing systems or obligations must remain compatible.

## Comprehensive coverage screen

Screen every area using applicability `Applicable`, `Not applicable`, or `Unknown`, with a basis or reason. Then track individual decisions as confirmed, proposed, or unknown. Triggers below indicate relevance, not the answer.

| Area                           | Relevance signals                                                               | Example next question                                                            |
| ------------------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| System behavior and boundaries | Any system implementing PRD behavior                                            | What observable state must remain after this operation fails partway through?    |
| Identity and permissions       | Actors, restricted files, accounts, roles, tenants, or privileged actions       | Which boundary must prevent one actor from accessing another actor's data?       |
| Data and integrity             | Inputs, stored/generated data, concurrent writes, or transactions               | Which invariant must remain true if two updates occur together?                  |
| Data lifecycle and privacy     | Personal/sensitive information, storage, exports, or deletion                   | Under the PRD's deletion requirement, what retained copies must also be removed? |
| Interfaces and integrations    | APIs, files, devices, events, imports/exports, or external services             | What outcome is required if the same message is delivered twice?                 |
| Security and abuse             | Untrusted input, public access, sensitive information, or consequential actions | What must the system do when this input is unauthorized or malicious?            |
| Compliance and policy          | Contractual, organizational, regulatory, or safety obligations                  | Which identified policy and version defines the required control?                |
| Performance and capacity       | Time-sensitive work, volume, limited compute/storage, or resource ceilings      | What workload must the response-time requirement hold under?                     |
| Reliability and recovery       | State changes, dependencies, data-loss risks, or service obligations            | What data loss is acceptable after the failure described here?                   |
| Operations and observability   | Support, deployment, monitoring, auditing, or ongoing ownership                 | What evidence must operators have to detect this failure?                        |
| Migration and rollout          | Existing data/users, replacements, cutovers, or phased exposure                 | What must remain recoverable if the migration is rolled back?                    |
| Compatibility and clients      | Multiple clients, platforms, protocol versions, or offline behavior             | Which existing client versions must continue to work?                            |
| Accessibility and localization | Human-facing interfaces or outputs, locales, or regional formatting             | Which accessibility conformance requirement applies to this output?              |
| AI and automation              | Probabilistic output, generated content, decisions, or tool execution           | Which actions require human authorization before execution?                      |
| Domain-specific constraints    | Payments, hardware, physical environment, offline synchronization, or safety    | What domain invariant must hold even when a dependency fails?                    |

Question examples assume their premises are established; adapt them rather than introducing unsupported obligations. A product-facing answer that would change the PRD must take the PRD handoff path.

Do not assume that a local tool has no security or privacy concerns, that a service needs a particular availability target, or that a product uses AI. For consequential unknown applicability, ask before omitting. Group low-risk exclusions with clear rationale instead of forcing separate chapters.

## Turning gaps into verifiable obligations

For an essential operation, establish the missing trigger, preconditions, inputs, result, state changes, permission boundaries, and relevant exceptions. Consider invalid input, duplicate/concurrent operations, timeouts, partial failure, and dependency outages proportionately. Do not enumerate every imaginable failure.

For a quality requirement, establish missing measurement conditions one at a time:

- What operation or system boundary is measured?
- Which workload or dataset represents the required operating range?
- In which environment must the requirement hold?
- What threshold is supported by user needs, a contract, policy, or evidence?
- Over what measurement window or distribution is it assessed?
- What evidence would demonstrate a pass or fail?

Not every criterion requires every measurement field. An inspectable encryption requirement and a latency distribution require different evidence. Product outcome metrics stay in the PRD; technical measurement explains how the system will satisfy relevant obligations.

If a target is unknown, offer a labeled proposal with a rationale or a next action to gather evidence. Do not fabricate benchmarks. A proposed number does not become confirmed merely because it appears in a draft.

## Handling uncertainty and changes

- For "I don't know", propose meaningful alternatives, an evidence-gathering action, or explicit deferral. Do not repeat the same question without new information.
- For conflicting sources, show the conflicting claims and their origins; ask which authority should resolve them. Do not silently prefer the newest-looking document.
- For scope expansion or a weakened PRD criterion, identify the affected product reference and obtain a PRD decision first. A technical workaround cannot redefine product acceptance implicitly.
- For technical decisions within the PRD scope, update requirements, acceptance, traceability, constraints, and risks together. Preserve stable IDs and record material changes.
- For deferred gaps, record the impact, implementation/release blocking status, and known owner or next action. Unknown impact is not automatically nonblocking.

## Checkpoints and stopping

Use brief checkpoints after establishing the baseline, after a material boundary or contract decision, and before finalizing. Ask for confirmation of one consequential interpretation, not blanket sign-off on unrelated unresolved decisions. Do not redisplay the full document after each answer.

Stop when requested or when the intended readiness level is supported and consequential decisions are confirmed. Save an already-started draft at the authorized path when possible. On resumption, reread the current PRD and TRD, detect baseline drift, and continue from the most important unresolved gap rather than restarting the interview.
