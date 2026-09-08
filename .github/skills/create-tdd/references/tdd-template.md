# TDD template

Use this template only after the PRD and TRD prerequisites in the skill workflow are satisfied. It does not authorize a standalone TDD from code or a placeholder for missing requirements.

Keep the core coverage, merging headings for a small design note. Expand conditional modules only where they help implement or review consequential choices. Replace placeholders with sourced information, a labeled proposal, or a meaningful unknown; remove instructional text and unused example rows. Example identifiers are a scheme, not design decisions to copy.

## Core outline

```markdown
# [Product or feature] - Technical design document

## Document control

| Field | Value |
| ----- | ----- |
| Version | [Document version, confirmed or proposed] |
| Status | Draft / Review-ready / Implementation-ready |
| Owner | [Known owner and role, or unknown] |
| Reviewers | [Known reviewers and roles, or unknown] |
| Last updated | [Actual update date] |
| Sign-off | [Explicit approval and scope for this version, or pending / unknown] |
| Intended audience | [Who uses this TDD and the design review or implementation scope it supports] |
| Release scope | [The PRD/TRD release or feature scope this design covers] |
| PRD baseline | [Source, version/revision or unknown, stated status, date consulted] |
| TRD baseline | [Source, version/revision or unknown, stated status, date consulted] |
| Implementation baseline | [Repository/revision and relevant components; no existing code, or inaccessible, where applicable] |

## 1. Design context and scope

[Brief technical purpose and design boundary. Link to product intent and technical obligations instead of repeating the PRD/TRD.]

- In scope: [Affected capabilities, components, and release scope.]
- Non-goals: [Design exclusions consistent with the requirements.]
- Design drivers: [The TRD requirements and sourced constraints that shape the solution.]
- Current versus target state: [What exists, what changes, and what remains unchanged.]
- Source limitations: [Partial excerpts, unavailable code/documents, unknown revisions, and their impact.]

| Constraint / dependency | Source and status | Design impact |
| ----------------------- | ----------------- | ------------- |
| [Actual platform, policy, contract, accepted ADR, or external dependency] | [Reference and confirmed / proposed / unknown status] | [Affected design choices] |

[Separate existing conventions and preferences from binding constraints. Check that the PRD and TRD govern the same scope.]

## 2. Proposed solution

### Architecture and responsibilities

[Explain the simplest credible solution, major boundaries, dependencies, and why it fits the design drivers. Add an inline diagram only if it clarifies the design.]

| Design ID | Component or mechanism | Responsibility and owned state | Interfaces / dependencies | Requirement or constraint references | State / basis |
| --------- | ---------------------- | ------------------------------ | ------------------------- | ------------------------------------ | ------------- |
| DES-001 | [Existing or proposed element] | [Responsibility, state owner, and trust boundary where relevant] | [Contracts and dependencies] | [TRD IDs or authoritative sources] | [Confirmed / proposed / unknown, with evidence] |

### Runtime behavior and failure handling

[Walk through essential flows using design and TRD references. Describe input/output, validation and authorization, state transitions, transaction/concurrency boundaries, and relevant duplicate, timeout, partial-failure, and recovery paths. Include algorithms or pseudocode only where correctness depends on them.]

### Applicable design detail

[Expand the conditional modules below here or into separate sections. Explain mechanisms, not merely aspirations such as "secure" or "scalable". Link authoritative contracts and existing specifications rather than duplicate them.]

### Coverage disposition

| Design area | Applicability | Basis / reason | Design or gap references |
| ----------- | ------------- | -------------- | ------------------------ |
| [Area from the interview guide] | Applicable / Not applicable / Unknown | [Evidence, exclusion rationale, or uncertainty] | [DES IDs, section, or open question] |

[Screen every area proportionately; group related low-risk exclusions when their reasons remain clear. Applicability is separate from whether a design is confirmed.]

## 3. Alternatives and decisions

### DEC-001: [Significant choice]

- Context and drivers: [Affected TRD requirements, existing decisions, and constraints.]
- Status: [Proposed / accepted / superseded; preserve an existing documented scheme if present.]
- Confirmation: [Who accepted what and when, with source; or pending / unknown.]
- Options considered: [Credible alternatives and relevant tradeoffs; include retaining the current approach where viable.]
- Recommendation / chosen approach: [Clearly distinguish the proposal from an accepted decision.]
- Rationale and evidence: [Why it meets the drivers; distinguish analysis, observed evidence, and assumptions.]
- Consequences: [Benefits, limitations, risks, operational/cost implications, and reversibility where relevant.]
- Related ADR: [Actual link, none, or inaccessible; record its stated status and scope.]
- ADR candidate: [Yes with reason, or no; this does not create an ADR.]

[Repeat only for consequential decisions. Do not manufacture alternatives for trivial or mandated choices. Preserve the history of superseded decisions and do not imply that TDD edits supersede accepted ADRs.]

## 4. Requirement coverage and verification strategy

| Requirement at baseline | Design references | Coverage and rationale | Verification approach / required evidence | Evidence state / gaps |
| ----------------------- | ----------------- | ---------------------- | ----------------------------------------- | --------------------- |
| [TRD ID/section, or PRD reference explicitly retained by the TRD without technical elaboration] | [DES IDs, decision, or section] | [New design, unchanged mechanism with source, or explicit gap] | [Reference the governing acceptance criteria and describe how the mechanism will be evaluated] | [Planned / available with actual reference / unknown; blocker if applicable] |

[Cover every in-scope TRD obligation, including PRD obligations it retains without a separate technical requirement. An unchanged mechanism still needs evidence or an explicit evidence gap; "no new code" or "no technical elaboration" does not waive the requirement. Preserve existing requirement IDs; if absent, cite the source section and revision rather than editing upstream just to add IDs.]

[Consequential design elements trace back to requirements or other authoritative constraints relevant to this scope. Identify unnecessary complexity or unsupported scope instead of inventing requirements to justify it.]

[For applicable quality requirements, explain the mechanism or analysis supporting feasibility under the TRD's measurement conditions. Do not replace thresholds or fabricate benchmarks. Identify feasibility experiments needed before implementation separately from verification evidence expected before release. Proposed experiments are not executed work.]

## 5. Risks, unresolved questions, and readiness

| ID | Issue / assumption | State and source | Affected references | Impact | Blocks implementation / release? | Owner / next action |
| --- | ------------------ | ---------------- | ------------------- | ------ | -------------------------------- | ------------------- |
| Q-001 | [Design risk, evidence gap, requirement conflict, or unknown] | [Confirmed / proposed / unknown, with basis] | [PRD/TRD, DES, DEC, or ADR references] | [Consequence if wrong or unresolved] | [Yes / no / unknown for each relevant gate, with reason] | [Known owner, upstream handoff, evidence action, or explicit deferral] |

### Readiness assessment

- Supported status: [Draft / Review-ready / Implementation-ready, with basis from the checklist.]
- Material blockers: [Explicit list, or none only when supported.]
- Confirmation / approval: [Confirmed scope, obligations, and consequential design choices; distinguish pending decisions.]
- Review limitations: [Unavailable context, unresolved findings, and untested assumptions.]
- Deferred nonblocking work: [Known next actions or agreed deferrals with reasons; distinguish later release evidence.]

[A proposed architecture is not an approved design. Readiness does not mean tests passed, release is authorized, or implementation may begin without a separate request.]

## 6. Material changes and references

### Decisions and material changes

| Date | Change or superseded decision | Basis / confirmed by | Affected baseline and design references |
| ---- | ----------------------------- | -------------------- | --------------------------------------- |
| [Actual date] | [Material design change or upstream drift] | [Source or explicit confirmation] | [PRD/TRD revisions, DES/DEC IDs, and relevant ADRs] |

[Preserve stable IDs and unrelated content. Do not reuse retired IDs or silently remove design coverage when a requirement changes. Record the reconciled outcome and reassess readiness.]

### References and glossary

[List the baselines, implementation evidence, ADRs, contracts, policies, and specifications actually consulted. State access limitations. Define terms only where useful; do not invent links or copy sensitive data.]
```

## Conditional modules

These extend the proposed solution, not the requirements baseline. A module can be a short paragraph or a linked existing specification; do not create empty chapters or new artifacts just to complete the outline.

| Module                                   | Include when applicable                                                                                                                                                                | Keep elsewhere                                                                   |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Components and runtime                   | Component responsibilities, request/event flows, important algorithms, state transitions, concurrency, idempotency, error propagation, and recovery mechanisms                         | Exhaustive class listings, code walkthroughs, and tasks                          |
| Data and lifecycle                       | Storage choice, physical schemas, keys/indexes, transactions, consistency, caching/invalidation, retention/deletion mechanisms, and schema evolution                                   | Copied sensitive data or duplicated authoritative schemas                        |
| Interfaces and integrations              | Concrete API/event/file design, authentication, validation, versioning, errors, timeouts, retry/deduplication mechanisms, and contract ownership                                       | Full API tutorials and competing copies of existing specifications               |
| Security, privacy, and abuse             | Trust boundaries, authorization enforcement, tenant isolation, secret/data protection, audit design, abuse controls, and identified threat mitigations                                 | Credentials, unsupported compliance claims, and unrelated exhaustive assessments |
| Performance, capacity, and cost          | Resource model, bottlenecks, scaling/backpressure, workload assumptions inherited from TRD, capacity reasoning, and sourced or explicitly uncertain cost implications                  | Invented prices/benchmarks and new quality targets disguised as design           |
| Reliability and recovery                 | Fault isolation, consistency during disruption, retry budgets, degraded behavior, backup/restore and recovery mechanisms                                                               | Step-by-step incident or recovery runbooks                                       |
| Deployment and operations                | Deployment topology, configuration boundaries, health signals, logs/metrics/traces, alert design, operational ownership, and support mechanisms                                        | Deployment commands, task schedules, and full operating procedures               |
| Migration, rollout, and compatibility    | Existing data/client compatibility, expand/contract sequencing, backfill/reconciliation, cutover, staged exposure, rollback triggers and mechanisms, and irreversible-step mitigations | Sprint plans or promises of rollback without a workable mechanism                |
| Clients, accessibility, and localization | Client state and compatibility, accessible interaction mechanisms, locale/time-zone/encoding handling, and offline synchronization                                                     | Repeated personas, new product behavior, or exhaustive visual specifications     |
| AI and automation                        | Model/tool boundaries, retrieval and grounding, input/output validation, human authorization, fallbacks, evaluation design, and model/data versioning                                  | Unjustified AI adoption, invented quality results, or raw sensitive prompts/data |
| Domain-specific mechanisms               | Relevant payment invariants, device constraints, environmental limits, or safety mechanisms supported by the baseline                                                                  | Invented certifications or unrelated domain checklists                           |
