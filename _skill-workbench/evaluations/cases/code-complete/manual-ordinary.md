# Apply Code Complete to One Construction Slice

Use `$code-complete` as the project book lens for this task.

Design the first local production slice of an untrusted order-quote function. It must validate a closed customer kind, nonnegative integer cents, domestic/international shipping, and an optional expedited flag; return typed quote or field-specific validation errors; use integer arithmetic; and include boundary and invalid-input tests. Persistence, networking, performance tuning, and production resilience are out of scope.

Provide the smallest implementation shape and construction decisions. This is ordinary matched construction, not a disputed interpretation or complete audit.
