# OBEY A Philosophy of Software Design by John Ousterhout

## When to use

Use when the main risk is accidental complexity, shallow abstractions, leaky interfaces, or tactical patches.

## Primary bias to correct

Working code, small pieces, and familiar wrappers are not automatically simple.

## Decision rules

- Optimize for lower cognitive load and local understandability, not shorter files, familiar patterns, fewer lines, or clever compactness.
- Prefer deep modules; reject wrappers, layers, helpers, facades, and split-outs that do not hide real complexity.
- Hide volatile decisions, representations, storage, protocol facts, workflow bookkeeping, and messy edge handling in one owning module.
- Make interfaces caller-centered and semantic; avoid staged APIs, flags, setup sequences, and mechanism leakage when the module can provide the right operation.
- If a change feels awkward or spreads widely, improve the boundary or abstraction instead of adding tactical special cases.
- Combine or split by total complexity: keep shared knowledge together and split only at independently understandable boundaries.
- Treat names and comments as design signals: precise abstraction names, explicit contracts, and no comments that compensate for bad decomposition.
- Adopt trends, patterns, or frameworks only when they reduce complexity; require evidence before performance tradeoffs, preserve behavior through public-contract tests, and eliminate exception cases through stronger interfaces or invariants.

## Trigger rules

- When adding a helper, layer, option, callback, pattern, or abstraction, prove it removes complexity for callers.
- When an API requires sequencing, representation, storage, transport, caching, protocol, or file-format knowledge, redesign the boundary.
- When names reveal mechanisms, comments get complicated, or code surprises readers, treat it as design evidence.
- When one change spreads widely, look for information spread, hidden dependencies, temporal coupling, or complexity pushed to callers.
- When optimizing, require evidence for the performance tradeoff and hide optimization details behind a stable interface.
- When adding an exception path, first try to eliminate it by changing the interface or invariant; otherwise keep it isolated from the normal path.

## Final checklist

- Fewer concepts to hold?
- More complexity hidden below the right boundary?
- Fewer special cases, knobs, leaks, and call-order traps?
- Better names and contracts, complexity kept in one place, and evidence for any performance tradeoff?
