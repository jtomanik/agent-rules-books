# Resolve a Missing-Concept Source Dispute

Inside an established Fulfillment context, one `ALLOCATED` state currently means either a replaceable proposed warehouse or an accepted stock reservation that requires an explicit release. The same state drives customer promises, warehouse work, and cancellation rules.

Two reviewers disagree about the exact source guidance:

- One says clearer status names are sufficient because both situations still belong to one allocation lifecycle.
- The other says the source's deeper-model and implicit-concept guidance requires an explicit concept when the distinction explains materially different business behavior and removes procedural special cases.

Resolve only this source-interpretation dispute. State the source conditions that justify a missing concept rather than a rename, the explanatory gain the proposed model must provide, and two or three domain-language scenarios that could falsify it. Keep any migration incremental and behavior-preserving; do not perform a complete domain-model audit.
