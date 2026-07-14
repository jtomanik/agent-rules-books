Refactor this existing export workflow without changing observable behavior.
Characterization tests already cover successful exports, malformed input, and
cleanup after a failed write.

```text
ExportController -> ExportService -> ExportCoordinator -> ExportWriter
```

Each object exposes one method and forwards the same mutable `ExportContext`.
Callers must invoke `initialize`, `load`, `normalize`, `write`, and `cleanup` in
order. The context exposes temporary paths, parser state, output format, and a
`cleanupRequired` flag. The same five-step sequence appears in three commands.

Plan a sequence of small, reversible, testable transformations that preserves
behavior while moving toward one deeper export operation with a caller-centered
contract. State the stopping condition and how each step proves that the new
boundary hides more complexity than it adds.
