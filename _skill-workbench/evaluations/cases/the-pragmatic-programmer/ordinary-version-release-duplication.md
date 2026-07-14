# Remove Version and Release Duplication

Review this routine packaging change and recommend a scoped correction.

```bash
# scripts/build-package.sh
VERSION="2.8.0"
sed "s/__VERSION__/$VERSION/" package.template.json > package.json
npm test
npm pack
```

```yaml
# .github/workflows/release.yml
env:
  VERSION: 2.8.1
steps:
  - run: npm test
  - run: npm pack
  - run: scp *.tgz "$RELEASE_HOST:/incoming"
  - run: ssh "$RELEASE_HOST" promote-latest
```

```text
RELEASE.md
1. Change VERSION in scripts/build-package.sh.
2. Change VERSION in release.yml.
3. Run npm test and npm pack locally.
4. Upload the archive.
5. Ask operations to run promote-latest.
```

The version mismatch has already produced one incorrectly labeled archive.
Keep the answer limited to ownership of the version fact, orthogonality of the
build and promotion steps, automation, and the fastest useful verification.
