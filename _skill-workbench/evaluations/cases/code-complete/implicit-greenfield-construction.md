# Design a Greenfield Import Module Before Implementation

Design the first production slice of a new in-process import module. No implementation exists yet. Before coding, the team must jointly settle:

- how untrusted JSON is validated into a typed record,
- whether invalid records fail the batch or produce per-record outcomes,
- how duplicate record IDs are represented,
- the routine and control-flow shape,
- the error contract exposed to the caller,
- the smallest integration boundary with an already-typed repository,
- and the boundary, invalid-input, duplicate, and mixed-result tests required for the first merge.

Persistence behavior, deployment, distributed delivery, retries, performance tuning, and production failure policy are out of scope.

Recommend the construction decisions and smallest reviewable implementation slice before coding begins. Do not perform a complete book audit or edit files.
