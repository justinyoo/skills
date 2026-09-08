# Adaptive interview guide

This is a question bank, not a script. Use supplied context first, skip answered questions, and ask one focused question at a time. An answer may resolve several gaps; update all affected areas instead of asking the remaining questions by rote.

## Choosing the next question

Prefer questions whose answers could change the product direction, release boundary, important user behavior, risk, or acceptance criteria. Resolve a contradiction before refining details that depend on it. Explain why a question matters when that would help the user answer.

Use plain language rather than asking the user to supply product-management terminology. Offer choices when the alternatives are meaningful, but do not steer the user into confirming an unsupported assumption.

## Foundation questions

Choose the first unanswered, consequential question; do not ask this whole list.

| Area              | Example question                                                   |
| ----------------- | ------------------------------------------------------------------ |
| Problem           | What is the main difficulty this product should remove?            |
| Primary user      | Who experiences that difficulty most directly?                     |
| Current workflow  | How does that person handle it today?                              |
| Evidence          | What have you observed that shows this problem matters?            |
| Outcome           | What should become possible or meaningfully better for that user?  |
| Context           | Is this a new product or a change to an existing one?              |
| PRD audience      | Who will use this document to make a decision?                     |
| Scope             | What is the smallest useful result the first release must deliver? |
| Non-goal          | What outcome are you deliberately not trying to achieve?           |
| Release exclusion | Which capability should explicitly stay outside this release?      |
| Constraint        | Is there a fixed constraint that could change what we can deliver? |

## Outcomes and measurement

Start with the outcome, not an arbitrary numerical target.

- What observable change would convince you this solved the problem?
- How could that change be measured?
- What is the current baseline, if known?
- What target would count as success?
- Over what period should the outcome be evaluated?
- What must not get worse while improving this outcome?

Ask these separately only where needed. If a baseline or target is unknown, record that fact and ask about a way to establish it when consequential. Do not substitute invented numbers or generic industry benchmarks.

## Requirements and journeys

For each essential journey, clarify only the missing behavior:

- What starts this journey?
- What must the user be able to accomplish?
- What should the user see when the action succeeds?
- What should happen when no results or data are available?
- What should happen when the action cannot be completed?
- Who is allowed to perform this action?
- What limit or boundary changes the expected behavior?
- If this capability were removed, would the release still be useful?

Turn the answers into requirements with observable acceptance criteria. Ask about important exceptions rather than enumerating every imaginable edge case. Avoid choosing databases, frameworks, or algorithms unless an actual constraint makes the choice relevant to the product requirement.

## Conditional modules

Screen every module against known context, then investigate only applicable or consequentially uncertain areas. A trigger identifies relevance, not permission to assume the answer. Record a reason for consequential exclusions.

| Module                             | When to explore                                                             | Example next question                                                   |
| ---------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| UX and accessibility               | Human interaction, including user-facing outputs from APIs or automation    | Does the primary journey need to work without a mouse?                  |
| Identity and permissions           | Accounts, multiple roles, shared resources, restricted actions              | Who should be allowed to view another user's information?               |
| Data and privacy                   | Personal, sensitive, uploaded, generated, or retained information           | What information must the product retain after the task ends?           |
| Data lifecycle                     | Stored information, exports, deletion requests, retention obligations       | What should happen to stored information when an account is deleted?    |
| Security and abuse                 | Untrusted input, public access, valuable actions, sensitive information     | What misuse would cause the greatest harm to users?                     |
| Performance and scale              | Time-sensitive interactions, large volumes, resource limits                 | How long can a user reasonably wait for the primary action to complete? |
| Reliability and recovery           | State changes, external dependencies, availability needs                    | What should users experience if the external service is unavailable?    |
| Integrations                       | External systems, APIs, imports, exports, synchronization                   | What should happen when the two systems disagree about a record?        |
| Migration and compatibility        | Replacing existing behavior, existing users or data, supported environments | Which existing user behavior must continue working unchanged?           |
| Payments and entitlements          | Charges, subscriptions, quotas tied to payment                              | What access should a user retain after a payment fails?                 |
| Localization and regional behavior | Multiple languages, regions, time zones, or formats                         | Which languages must the first release support?                         |
| Compliance and policy              | Regulated domains, organizational policy, contractual obligations           | Which known policy or regulatory obligation constrains this release?    |
| AI behavior and evaluation         | Probabilistic output, generated content, automated decisions or actions     | What should happen when the system cannot produce a reliable result?    |
| Operations and rollout             | User exposure, feature enablement, monitoring, support ownership            | What signal should cause a rollout to pause?                            |

For sensitive or high-risk products, also clarify relevant access boundaries, human review, failure safeguards, and the evidence needed to assess behavior. For AI products, clarify evaluation examples, unacceptable outputs, and action authorization where applicable. Do not claim compliance or safety certification from an interview; record review obligations and unresolved expert decisions.

## Handling uncertainty and disagreement

- If the answer is "I don't know", offer a concrete alternative, a clearly labeled proposal, or an explicit deferral. Do not ask the same question repeatedly.
- If sources conflict, present the conflicting claims with their sources and ask which should govern the PRD.
- If the user changes a decision, update dependent scope, requirements, metrics, and risks together. Preserve requirement IDs and record the material change.
- If a suggestion would materially expand scope, ask for a decision before turning it into a requirement.
- If a gap is deferred, record its impact and whether it blocks implementation. Ask for an owner or next action only when useful; unknown owners remain unknown.

## Checkpoints and stopping

Use short checkpoints after the foundation, after material scope decisions, and before finalizing. Ask for confirmation of a particular interpretation or decision, not a blanket approval of several unrelated unresolved questions.

Stop interviewing when the user requests a pause or stop, or when the requested readiness level is supported and consequential decisions have been confirmed. Save the draft with its honest status. When resuming, read the current PRD and continue from the highest-impact unresolved gap rather than restarting.
