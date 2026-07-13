# Review One Derived Search Projection

Review only the ownership and recovery semantics of this product update path. Recommend the smallest design correction. This is not a complete platform, production-readiness, or architecture-layer audit.

```ts
export async function renameProduct(
  productId: string,
  name: string,
): Promise<void> {
  await products.update(productId, { name });

  try {
    await search.documents.update(productId, { name });
  } catch (error) {
    logger.warn({ error, productId }, "search update failed");
  }
}
```

Facts:

- PostgreSQL `products` is the declared authority for product names.
- Search results may be stale for up to ten minutes.
- PostgreSQL logical change data capture is already available.
- The search index has no full rebuild command and no durable projection checkpoint.
- A failed direct search update is currently repaired only when another product edit happens.
- The API contract for the rename is successful once the PostgreSQL transaction commits.

State whether the direct dual-write is acceptable under those facts and identify the minimum propagation, lag-visibility, rebuild, and repair contract needed.
