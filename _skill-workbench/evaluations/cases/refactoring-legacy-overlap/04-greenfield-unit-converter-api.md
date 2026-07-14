# Design a Greenfield In-Memory Unit Converter API

Design the public API for a new in-memory unit-conversion library. There is no existing implementation, migration, compatibility surface, or legacy data.

Requirements:

- Support user-supplied definitions for units belonging to a dimension.
- Support scale and offset conversions, including absolute temperatures.
- Reject unknown units, incompatible dimensions, duplicate definitions, invalid scales, and non-finite inputs.
- Keep conversion deterministic and free of I/O or global registration.
- Allow a configured converter to be shared safely by concurrent callers.
- Leave parsing, formatting, compound-unit algebra, dynamic exchange rates, and localization out of scope.

Compare two or three credible interface shapes and recommend one. Define the important types, error contract, mutability model, and test surface. This is API design for new code, not an implementation request.
