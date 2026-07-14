# Catalog Diagnosis Plus A Safe Change Sequence

The current tests cover CSV and JSON output byte for byte. The team wants to add XML next, but first wants a behavior-preserving structural change.

```ts
abstract class Exporter {}
class CsvExporter extends Exporter {}
class JsonExporter extends Exporter {}

abstract class Formatter {}
class CsvFormatter extends Formatter {}
class JsonFormatter extends Formatter {}

function formatterFor(exporter: Exporter): Formatter {
  if (exporter instanceof CsvExporter) return new CsvFormatter();
  if (exporter instanceof JsonExporter) return new JsonFormatter();
  throw new Error("unsupported exporter");
}
```

The proposed XML change would add both `XmlExporter` and `XmlFormatter` and another branch.

First classify the catalog smell and compare its preferred, fallback, and risky treatments. Then provide a small, reversible, behavior-preserving refactoring sequence using the supplied tests, with verification checkpoints after risky moves, public compatibility handling, and a stopping condition before XML behavior is introduced. Keep the smell-to-treatment judgment separate from the safe transformation sequence.
