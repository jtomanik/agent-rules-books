Choose between these two APIs for a local image-thumbnail module and justify
the choice.

```ts
// Candidate A
const decoded = decodeImage(bytes, codec);
const resized = resizePixels(decoded.pixels, width, height, algorithm);
const encoded = encodeImage(resized, outputFormat, quality);

// Candidate B
const thumbnail = createThumbnail(bytes, {
  maxWidth: 320,
  maxHeight: 320,
  output: "webp",
});
```

The module owns codec selection, aspect-ratio preservation, orientation
normalization, temporary buffers, and quality defaults. Ordinary callers need
only a bounded thumbnail in the requested output format. A diagnostics tool
occasionally needs decoded pixel access, but the production path does not.

Recommend the public interface, placement of the exceptional diagnostics need,
and tests that protect the contract without exposing internal stages.
