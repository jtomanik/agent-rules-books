# Implement a Fully Specified Local Function

Implement and review only this function. The contract is complete, there are no external boundaries or dependencies, and no broader construction, architecture, debugging, refactoring, reliability, or performance decision is requested.

```ts
export function clamp(value: number, minimum: number, maximum: number): number {
  throw new Error("not implemented");
}
```

Required behavior:

- Assume all three inputs are finite numbers and `minimum <= maximum`.
- Return `minimum` when `value < minimum`.
- Return `maximum` when `value > maximum`.
- Otherwise return `value` unchanged.

Provide the implementation and three representative tests. Do not edit files.
