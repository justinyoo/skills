# Adaptive TDD interview guide

This is a coverage screen and question bank, not a fixed questionnaire. Read the PRD, TRD, relevant decisions, and available implementation context first. Investigate what can be answered from those sources, propose a reasoned design, and ask one focused question at a time about consequential gaps.

## Context and prerequisites

### Baseline gates and handoffs

| Situation                                                              | Next action                                                                                                                          |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| No PRD or TRD                                                          | Ask to create the PRD first with `create-prd`; after reading it, ask to create the TRD with `create-trd`. Do not draft a TDD yet.    |
| TRD exists without a PRD                                               | Ask to supply or create the PRD, then obtain authorization to reconcile the existing TRD. Do not infer the PRD from the TRD or code. |
| PRD exists without a TRD                                               | Ask to create the TRD with `create-trd`, supply one, or pause.                                                                       |
| A required source is inaccessible                                      | Request an accessible copy or sufficient excerpt and disclose its limits; do not claim absence or fabricate the content.             |
| Multiple sources, conflicting scopes, or missing essential obligations | Ask which baseline governs or route the foundational gap to the owning document before drafting.                                     |
| Both draft baselines establish a coherent foundation                   | Begin a draft design; keep nonfoundational gaps explicit instead of requiring blanket approval or a fully designed TRD.              |
| No existing implementation                                             | Design from the requirements and confirmed constraints; do not invent repository evidence.                                           |
| User declines the prerequisites or stops                               | Pause without further questions or a placeholder TDD. Save only an already-started authorized draft.                                 |

With a question tool, offer creating the missing prerequisite, supplying it, or pausing as separate choices. Invoke a companion skill or follow its accessible instructions only with permission. If unavailable, explain the limitation and request the document or pause.

Example opening when the PRD exists but the TRD does not:

> The TDD needs the technical obligations and acceptance conditions that govern the design. Would you like to create the companion TRD first?

### Investigation before interview

| Source                         | Inspect for                                                                                                                                                               | Do not infer                                            |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| PRD and TRD                    | Governing scope, stable references, required behavior, quality conditions, actual constraints, open decisions, and PRD obligations retained without technical elaboration | Approval from a filename or a generated document        |
| Existing design and code       | Affected components, reusable patterns, state ownership, boundaries, and current behavior                                                                                 | That all current behavior is intended or suitable       |
| Contracts and dependencies     | Compatibility requirements, actual versions/declarations, and integration limitations                                                                                     | Runtime guarantees from a dependency declaration alone  |
| Tests and operational evidence | Existing expectations, covered failure paths, and actual evidence sources                                                                                                 | That read tests passed, or that planned evidence exists |
| ADRs and policies              | Applicability, status, authority, consequences, and supersession links                                                                                                    | That every old or proposed decision is binding          |

Stay within the authorized scope. If external research, experiments, or unavailable sources are needed, identify the evidence gap and obtain the appropriate authorization or accessible material rather than silently expanding the task.

## Choosing the next question

Ask first about conflicts or uncertainty that could invalidate the solution, then costly-to-reverse choices and failure behavior, then feasibility and operational mechanisms. Refine low-impact details only when needed to implement or review the design.

Offer a recommendation and credible alternatives with relevant tradeoffs. Explain the source and uncertainty behind the recommendation. Do not ask "Which database/framework/cloud?" before checking for existing constraints and whether a new choice is necessary.

| Question type           | Example                                                                                      | Where the answer belongs                                                             |
| ----------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Product decision        | Must users be able to undo a completed operation?                                            | PRD first when not established; then reconcile TRD/TDD                               |
| Technical obligation    | What result must a retry return after the operation already completed?                       | TRD, consistent with the PRD                                                         |
| Implementation decision | Should the deduplication record and business change commit in the same transaction?          | TDD, evaluated against the established retry and integrity obligations               |
| Decision authority      | Which owner can authorize a departure from this accepted ADR?                                | Explicit decision/handoff; the agent cannot supersede it                             |
| Feasibility evidence    | May we run a bounded prototype to determine whether this mechanism meets the existing limit? | Separate authorized evidence-gathering action; record planned versus actual evidence |

These examples assume their premises are established; do not introduce requirements merely to ask the question.

## Comprehensive coverage screen

Screen every area as `Applicable`, `Not applicable`, or `Unknown`, with a reason. Track confirmation of each choice separately. A small local tool still needs proportionate consideration of permissions, sensitive files, failed writes, and output integrity; it does not automatically need service scaling or a deployment platform.

| Area                                     | Investigate or propose first                                                                             | Example next question if unresolved                                                                       |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Boundaries and responsibilities          | Existing component ownership, trust boundaries, and the smallest change satisfying the TRD               | Which existing component is authorized to own this new state?                                             |
| Runtime and concurrency                  | Essential flows, atomicity, invariants, ordering, duplication, and partial-failure paths                 | Is the proposed transaction boundary compatible with the established ownership constraint?                |
| Data and lifecycle                       | Storage/schema/index design, consistency, caching, deletion, and retained copies                         | May we change the shared schema, or must this design remain backward-compatible with its current writers? |
| Interfaces and integrations              | Existing contracts, versioning, authentication, validation, timeouts, retries, and deduplication         | Can the external consumer adopt the proposed contract version during rollout?                             |
| Security, privacy, and abuse             | Enforcement points, least privilege, tenant isolation, data protection, and abuse controls               | Does the platform support the proposed per-tenant enforcement mechanism?                                  |
| Performance and capacity                 | Bottlenecks, resource bounds, backpressure, and reasoning under the TRD workload                         | May we prototype this mechanism to resolve the feasibility risk against the existing latency requirement? |
| Cost and dependencies                    | Existing capabilities, added operational/licensing burden, and sourced estimates if available            | Is the proposed managed dependency permitted under the documented platform policy?                        |
| Reliability and recovery                 | Fault isolation, bounded retries, degraded modes, backup/restore, and data-loss behavior                 | Who can confirm whether the existing restore mechanism covers the new state?                              |
| Deployment and operations                | Topology, configuration/secret boundaries, health/telemetry signals, and support ownership               | Can the current deployment platform support the proposed traffic-switch mechanism?                        |
| Migration and rollback                   | Mixed-version behavior, backfill, reconciliation, irreversible steps, and rollback mechanisms            | Can old and new writers coexist during the proposed migration sequence?                                   |
| Clients, accessibility, and localization | Existing UI/client patterns, accessible interaction, locale/time-zone handling, and offline behavior     | Can we reuse the existing accessible interaction component for this workflow?                             |
| AI and automation                        | Justified model use, tool permissions, untrusted content boundaries, grounding, fallback, and evaluation | Can the proposed retrieval path enforce the existing document-access rules before model invocation?       |
| Domain-specific mechanisms               | Baseline-backed safety, financial, device, environment, or synchronization invariants                    | Which existing mechanism enforces this domain invariant during dependency failure?                        |
| Verification and feasibility             | TRD acceptance mapping, relevant test/evaluation strategies, and design-critical evidence gaps           | Does the available environment let us evaluate the identified failure mode without affecting real users?  |
| Decisions and evolution                  | Alternatives, reversibility, existing ADRs, and long-lived decision rationale                            | Does this decision apply beyond this feature and need to be flagged as an ADR candidate?                  |

A question about a missing target, obligation, or product behavior belongs upstream, even if encountered during this screen. Propose implementation mechanisms only within the established requirements.

## Developing alternatives and lightweight decision records

For each consequential choice:

1. Identify the requirement or constraint driving it and check existing accepted decisions.
2. Compare credible options on the dimensions that matter for this scope. Include retaining the current solution when viable; do not manufacture a fixed number of alternatives.
3. Recommend an approach with rationale, consequences, reversibility, and evidence limits. Label estimates, assumptions, and untested claims.
4. Ask for one unresolved consequential decision or evidence-gathering authorization, not approval of several bundled choices.
5. Record its status and confirmation basis, then update affected design and traceability.

An ADR is useful for a cross-system/team decision, a costly-to-reverse choice, a reusable standard, or rationale that should outlive the current TDD. Flag such candidates but do not automatically create records. A TDD decision summary must not become a competing source of truth for an accepted ADR.

## Handling uncertainty and changes

- For unknown answers, propose options, identify evidence needed, or agree to defer with an impact and next action. Do not invent targets, costs, performance results, owners, or consent.
- For requirement changes, obtain authorization for the PRD/TRD handoff before incorporating them as the new design baseline. Reconcile downstream documents after each authorized change.
- For conflicting ADRs or uncertain authority, preserve the conflict and affected design as unresolved; user preference alone does not prove that an organizational decision was superseded.
- For deferred issues, distinguish implementation blockers from release evidence expected later. Unknown impact must not silently become nonblocking.
- During review, correct source-supported drafting errors directly. Return unanswered decisions to the appropriate interview or upstream workflow.

## Checkpoints and stopping

- After material decisions, update component/flow design, alternatives, coverage, risks, and verification together. Briefly confirm a consequential interpretation instead of redisplaying the whole document.
- Stop when requested or when the intended readiness is supported. Save an authorized draft and state blockers without continuing questions after a stop.
- On resumption or an update request, reread current baselines and the TDD, preserve IDs and decision history, and assess drift before reusing the old readiness status.
