# Improve a Fully Specified Local Formatter

The behavior is complete, intentional, and covered by green tests. This helper has no I/O, shared state, asynchronous behavior, framework code, integration risk, tuning requirement, or unresolved construction decision. Preserve its exported signature and exact output.

```ts
export function displayTemperature(celsius: number, compact: boolean): string {
  // Work out which text to return based on compact mode.
  let result = "";

  if (compact) {
    result = celsius.toFixed(1) + "C";
  } else {
    const fahrenheit = (celsius * 9) / 5 + 32;
    result = celsius.toFixed(1) + " degrees Celsius / " + fahrenheit.toFixed(1) + " degrees Fahrenheit";
  }

  return result;
}
```

Provide the smallest local readability improvement and concise tests. Keep scope to naming, function shape, the boolean mode, and the flow-narrating comment. This is read-only analysis; do not edit files.
