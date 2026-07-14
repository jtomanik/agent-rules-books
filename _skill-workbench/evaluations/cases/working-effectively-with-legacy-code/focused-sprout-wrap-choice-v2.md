# Choose a Sprout or Wrap Technique for a Fragile Method

`settleBatch()` is a 900-line method with no focused tests. It reads records, applies old pricing rules, writes settlements, sends notifications, and updates a checkpoint. The database and notifier are hard-coded. A slow staging test covers one successful batch.

Product needs a new, independently testable fraud-decision calculation before settlement writes. Existing pricing and notification behavior must remain unchanged.

Resolve a bounded technique dispute: compare Sprout Method, Sprout Class, Wrap Method, and Wrap Class for this insertion. State the source conditions that favor each option, the minimum characterization or observation point needed first, and the smallest reviewable patch boundary. Do not redesign the batch processor or perform a complete legacy assessment.
