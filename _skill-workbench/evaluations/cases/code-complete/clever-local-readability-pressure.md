# Keep a Local Readability Fix Local Under Pressure

The behavior is complete and covered by focused green tests. A lead insists the helper remain a compact one-liner because the review must finish today. There is no unresolved boundary, error, integration, performance, architecture, or broader construction decision.

```ts
export const label = (name: string, compact: boolean): string => compact ? name.trim().toUpperCase() : "Customer: " + name.trim().toUpperCase();
```

Recommend the smallest readability improvement to naming, the boolean mode, and expression shape while preserving behavior. Do not widen the task into a general construction audit or edit files.
