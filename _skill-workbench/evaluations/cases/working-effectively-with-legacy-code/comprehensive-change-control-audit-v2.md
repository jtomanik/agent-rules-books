# Comprehensive Change-Control Audit for Poorly Understood Code

Perform a comprehensive end-to-end changeability audit of a decade-old settlement subsystem before a year-long rules program.

Behavior is poorly documented; tests are slow and broad; constructors open databases and files; static clocks and globals hide inputs; UI handlers contain business rules; large methods mix policy and I/O; side-effecting constructors make objects hard to instantiate; and teams usually edit production code first and verify in staging.

Cover behavior characterization, first feedback, test selection, seams, sensing and separation, dependency breaking, sprout and wrap techniques, specialized dependency-breaking options, risky databases/UI/globals/constructors, local refactoring heuristics, forbidden approaches, testing, code-generation choices, and final review. Optimize for understanding, control, and the smallest safe changes rather than a rewrite.
