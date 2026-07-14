# Add One Rule to a Deterministic Existing Calculator

An existing invoice calculator has no focused tests, but all collaborators are already passed through constructor interfaces and its public method is deterministic for supplied inputs. A slow end-to-end test covers one normal invoice. Production behavior for rounding and missing tax codes is relied upon but undocumented.

Product needs one new exemption for nonprofit customers. The requested change does not alter I/O, deployment, concurrency, or external failure behavior.

Choose the smallest safe change. State what current behavior to characterize first, where to place the new-behavior test, how to preserve any surprising relied-on behavior, and what local cleanup is justified after the rule works. Do not redesign the calculator or introduce a new architecture.
