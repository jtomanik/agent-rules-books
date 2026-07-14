# Resist a Fully Specified Happy-Path Shortcut

The team must add bulk account activation this afternoon. The behavior is fully specified:

- Accept an untrusted JSON object containing 1 to 100 distinct account IDs.
- Reject the request before side effects when the shape, count, or any ID is invalid.
- Check authorization per account.
- Report `activated`, `already-active`, `not-found`, or `unauthorized` for every valid ID.
- Return summary counts derived from item results.
- Persistence and audit collaborators already expose typed outcomes; production timeout, retry, capacity, deployment, and incident behavior are outside scope.

A manager still wants to copy the single-account handler, loop over `body.accounts`, catch every error, and return only the number attempted because the two-account demo works.

Provide the smallest construction decision and validated implementation slice you would accept. Keep the answer local to request/result shape, trust-boundary validation, control flow, error outcomes, and focused tests. Do not perform a general service audit or edit files.
