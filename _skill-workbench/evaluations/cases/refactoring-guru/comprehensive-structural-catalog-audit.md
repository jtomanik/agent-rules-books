# Complete Structural Catalog Audit

Perform an exhaustive code-smell and named-treatment audit of this maintenance area. Use all applicable packaged guidance for this catalog and read its complete source end to end, rather than stopping at compact guidance.

```ts
class OrderExporter {
  export(order: Order, format: "csv" | "json"): string {
    if (format === "csv") {
      return new CsvFormatter().format(order.customer.profile.name, order.lines, order.totalCents);
    }
    return new JsonFormatter().format(order.customer.profile.name, order.lines, order.totalCents);
  }
}

class CsvFormatter {
  format(name: string, lines: OrderLine[], totalCents: number): string {
    return `${name},${lines.length},${totalCents}`;
  }
}

class JsonFormatter {
  format(name: string, lines: OrderLine[], totalCents: number): string {
    return JSON.stringify({ name, lines: lines.length, totalCents });
  }
}

class ExportService {
  constructor(private readonly exporter: OrderExporter) {}
  export(order: Order, format: "csv" | "json"): string {
    return this.exporter.export(order, format);
  }
}
```

The next release may add XML. A separate vendor money class lacks one formatting operation, and three call sites currently duplicate the workaround. Existing characterization tests cover CSV and JSON output, but no XML behavior exists.

Cover timing and scope, technical debt, all relevant smell families, treatment priorities and alternatives, named-technique conditions, execution safety, compatibility, verification, anti-patterns, stopping, and the final review checklist. Separate current evidence from speculative future work.
