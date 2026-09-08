# TRD template

Use a lean core with conditional modules, not an exhaustive form to fill mechanically. This template is used only after the PRD prerequisite in the skill workflow is met. It does not authorize generating a TRD without a PRD.

Keep core coverage even when merging headings. Expand the applicable areas from the interview guide into the requirements section or separate chapters; there is no minimum page count. Replace placeholders with sourced content, a labeled proposal, or a meaningful unknown. Remove unused example rows and optional sections. Example IDs describe a naming scheme, not requirements to copy into the output.

## Core outline

```markdown
# [Product or feature] - Technical requirements document

| Field             | Value                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------- |
| Version           | [Document version, confirmed or proposed; distinct from product release]                    |
| Status            | Draft / Review-ready / Implementation-ready                                                 |
| Owner             | [Known owner, or unknown]                                                                   |
| Reviewers         | [Known participants, or unknown]                                                            |
| Last updated      | [Actual update date]                                                                        |
| Sign-off          | [Explicit approval for this version, or pending / unknown]                                  |
| Intended audience | [Who uses this TRD and for which decision]                                                  |
| PRD baseline      | [Source link or identifier, version/revision or unknown, stated status, and date consulted] |
| Release scope     | [The PRD release or feature scope this TRD covers]                                          |

## 1. Purpose and PRD relationship

[Brief technical purpose and intended system outcome. Reference the PRD's problem, users, goals, and scope rather than restating them.]

- Product source of truth: [PRD references governing this scope.]
- Source limitations: [Partial excerpts, unavailable context, or baseline uncertainty, if any.]
- Related artifacts: [Existing TDDs, ADRs, contracts, policies, or standards actually used.]

[Product intent and scope remain in the PRD. Any requested product change must be resolved there rather than introduced here as a conflicting technical requirement.]

## 2. Technical scope and system context

- In scope: [Systems, components, and technical responsibilities needed for the PRD scope.]
- Boundaries: [Actors, external systems, trust boundaries, and responsibility handoffs.]
- Out of scope: [Technical exclusions consistent with the PRD; link product non-goals.]
- Current versus required behavior: [Relevant differences for a change to an existing system.]

[Include a small context diagram or link only if it clarifies a boundary or obligation. Proposed implementation topology belongs in a TDD.]

## 3. Constraints, dependencies, and coverage

| ID     | Constraint or dependency                                              | State and source                             | Technical impact                      | Owner / next action |
| ------ | --------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------- | ------------------- |
| CD-001 | [Actual platform, policy, contract, resource, or delivery constraint] | [Confirmed / proposed / unknown, with basis] | [Affected obligations or feasibility] | [Known or unknown]  |

[Reference applicable standards and their versions where known. Separate binding constraints from preferences. Put unvalidated assumptions in section 6.]

### Coverage disposition

| Area            | Applicability                         | Basis / reason                                               | Requirement or gap references |
| ----------------| ------------------------------------- | ------------------------------------------------------------ | ----------------------------- |
| [Screened area] | Applicable / Not applicable / Unknown | [Evidence, exclusion rationale, or unresolved applicability] | [TRD IDs or open question]    |

[Screen all areas in the interview guide. Keep this compact; group related areas only when their applicability and rationale remain clear. An unknown is not an exclusion and need not create an empty chapter.]

## 4. Technical requirements

[Group requirements by relevant area. Add conditional modules below only where needed. Each obligation has one authoritative record; reference it from other sections rather than duplicating it.]

### TR-F-001: [Short, behavior-oriented title]

- State and source: [Confirmed or proposed; PRD ID/section and baseline, or other authoritative source.]
- Rationale: [Why this obligation is necessary for the PRD scope.]
- Priority / release scope: [Agreed or explicitly proposed; distinguish deferred work.]
- Requirement: [One clear obligation using "must", with relevant conditions.]
- Rules and boundaries: [Inputs, outputs, state changes, permissions, limits, and exceptions as applicable.]
- Acceptance criteria: [Observable pass/fail behavior, including relevant boundary, unauthorized, and failure cases.]
- Verification: [Test, inspection, analysis, or demonstration; conditions and evidence to collect or a verification reference.]
- Dependencies / unresolved details: [Related IDs, unknowns, and blocking impact.]
- Owner: [Known decision or verification owner, or unknown.]

[Repeat for necessary obligations. Use stable TRD-specific IDs such as TR-F-001 for behavior, TR-D-001 for data, TR-I-001 for interfaces, TR-Q-001 for quality/security, and TR-O-001 for operations. Preserve an existing document's unambiguous scheme. Do not renumber IDs to match display order or reuse retired IDs.]

[A quantitative criterion must define its relevant measurement boundary, workload/dataset, environment, window, and threshold, directly or by reference. If these are unknown, identify the gap; do not supply arbitrary numbers.]

## 5. Verification, acceptance, and traceability

### Product-to-technical coverage

| PRD ID or section at baseline | TRD requirement IDs        | Coverage disposition                                                                  |
| ----------------------------- | -------------------------- | ------------------------------------------------------------------------------------- |
| [In-scope PRD reference]      | [IDs, or none with reason] | [Covered, explicit gap, or no additional technical requirement needed with rationale] |

[Cover each in-scope product requirement, including relevant PRD quality requirements. "No additional technical requirement needed" retains the original PRD obligation and acceptance criteria; it does not waive them.]

### Technical-to-evidence mapping

| TRD ID   | Source / scope rationale                              | Verification reference or method                         | Conditions and expected evidence                    | Evidence state                                        |
| -------- | ----------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------- |
| [TRD ID] | [PRD reference or policy/contract/etc. and relevance] | [Acceptance/verification field above or linked artifact] | [Required conditions and evidence, or explicit gap] | [Planned / available with actual reference / unknown] |

[Reference authoritative acceptance criteria rather than maintaining conflicting copies. Do not invent test results, evidence links, or executed verification.]

### Technical release gates

[Required technical evidence or conditions before release, consistent with the PRD's release criteria. Include applicable integration, security, recovery, or migration gates. Keep detailed procedures and actual results in linked artifacts.]

[Product success metrics, requirement acceptance criteria, technical release gates, and document readiness are distinct. A ready TRD does not establish a tested or releasable system.]

## 6. Risks, unresolved decisions, and changes

### Assumptions, risks, and questions

| ID    | Type and issue                            | State / source                               | Affected PRD/TRD references | Impact                               | Blocks implementation or release?                        | Owner / next action                         |
| ----- | ----------------------------------------- | -------------------------------------------- | --------------------------- | ------------------------------------ | -------------------------------------------------------- | ------------------------------ |
| Q-001 | [Assumption, risk, conflict, or question] | [Confirmed / proposed / unknown, with basis] | [IDs or sections]           | [Consequence if unresolved or wrong] | [Yes / no / unknown, with reason for each relevant gate] | [Known or unknown; product gaps route to the PRD] |

[Make blockers prominent. Unknown owners, dates, or impact remain unknown rather than invented or automatically treated as harmless. Record agreed deferrals and consequential exclusions.]

### Decisions and material changes

| Date          | Decision or change                                    | Basis / confirmed by              | Affected PRD baseline and TRD IDs |
| ------------- | ----------------------------------------------------- | --------------------------------- | --------------------------------- |
| [Actual date] | [Decision, changed source, or superseded requirement] | [Source or explicit confirmation] | [Affected references]             |

[Preserve a concise change history, not the raw interview. Track PRD changes and reconcile dependent requirements, evidence expectations, and readiness.]

### Readiness assessment

- Supported status: [Draft / Review-ready / Implementation-ready, with basis.]
- Material blockers: [Explicit list or none only when supported.]
- Confirmation / approval: [Known confirmation and its scope; no inferred sign-off.]
- Review limitations: [Missing sources or unresolved findings, if any.]

### References and glossary

[Source documents, PRD baseline, standards and versions, contracts, and linked technical artifacts actually used. Define terms only where helpful; do not invent links or imply inaccessible sources were read.]
```

## Conditional modules

These extend section 4 or become separate chapters when depth warrants it. Use the same requirement record and traceability rules in every module. A module may be a short paragraph; do not create empty tables or unnecessary design work.

| Module                                   | Include when applicable                                                                                                                                                    | Keep elsewhere                                                                                    |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| System behavior and failure paths        | Technical inputs/outputs, state transitions, invariants, concurrency, validation, partial failure, and retry consequences supporting PRD journeys                          | Repeated user stories and detailed internal algorithms                                            |
| Data and lifecycle                       | Logical entities, ownership, formats, validation, integrity, classification, retention, deletion, export, and residency obligations                                        | Physical database schemas and storage-engine selection unless binding                             |
| Interfaces and integrations              | System/contract ownership, protocols and formats where required, authentication, compatibility/versioning, errors, timeouts, delivery guarantees, retries, and idempotency | Full API tutorials or duplicated authoritative schemas                                            |
| Security, privacy, and compliance        | Trust boundaries, access isolation, audit needs, secret handling, abuse constraints, applicable policy/standard versions, and required review evidence                     | Credentials, real sensitive examples, unsupported compliance claims, and exhaustive threat models |
| Performance, capacity, and resources     | Latency/throughput/resource bounds, scale envelope, workload profiles, measurement conditions, and degradation behavior                                                    | Arbitrary benchmarks and proposed tuning techniques                                               |
| Reliability and recovery                 | Availability measurement, fault handling, consistency during disruption, recovery time/data-loss objectives, and restore expectations                                      | Detailed resilience topology and recovery procedures                                              |
| Operations and observability             | Required signals, audit events, alertable conditions, support access, backup, deployability, and operational ownership                                                     | Monitoring vendor preferences and step-by-step runbooks                                           |
| Migration, rollout, and compatibility    | Required existing behavior, supported versions/platforms, data reconciliation, cutover conditions, reversibility, and rollback outcomes                                    | Task schedules and deployment command sequences                                                   |
| Accessibility, localization, and clients | Applicable standards, assistive/client compatibility, locale/time-zone/encoding behavior, and assessable output requirements                                               | Product audience discovery and exhaustive visual specifications                                   |
| AI and automated decisions               | Evaluation conditions and datasets, quality/failure bounds, uncertainty behavior, human oversight, tool/action authorization, and model/data lifecycle obligations         | Prompt implementation and model preference unless binding                                         |
| Domain-specific obligations              | Payment correctness, device/environment limits, offline operation, safety constraints, or other evidenced domain needs                                                     | Invented certifications and irrelevant domain checklists                                          |

Every area is screened, not automatically expanded. For instance, a small local tool still needs consideration of permissions, sensitive files, errors, and output integrity, but may have a justified exclusion for service availability or online rollout.
