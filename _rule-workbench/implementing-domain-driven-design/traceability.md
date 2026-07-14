# OBEY Implementing Domain-Driven Design by Vaughn Vernon

Canonical full source: [full.md](full.md)

## Compression decisions

- Re-run under the current `PROCESS.md` on 2026-05-02 for the 8th alphabetic book, `implementing-domain-driven-design`.
- Manually repaired on 2026-07-13 after pre-authoring reverse tracing found compressed-source defects in qualifiers, service and Repository semantics, cross-context boundaries, Aggregate triggers, and Domain Event remediation.
- This was a book-specific re-run, not a `PROCESS.md` bug. The process already requires source-faithful compression, current line ranges, section-by-section coverage, and explicit dispositions for merged or omitted material.
- No retained rule is labeled `default`; the source uses even generic-looking guidance to block common DDD failures: global models, fake Ubiquitous Language, ORM-shaped Aggregates, shared domain packages, generic Repositories, anemic Application Services, and unbounded cross-context coupling.
- `mini.md` keeps every rule that changes architecture, modeling, integration, persistence, testing, review, or repeated local implementation decisions.
- `nano.md` keeps only always-on guardrails for the highest-risk shortcuts under tight context: missing Bounded Context, language drift, shared model types, Aggregate sprawl, anemic services, Repository leakage, and client or foreign model pressure.
- Detailed code-generation, review, testing, and checklist lists are merged into operational rules, trigger rules, and final checklist items rather than repeated verbatim; every source subsection below now has a specific covered or intentionally-lost disposition.

## Activation and bias trace

- Mini activation is unchanged and routes work involving contexts, language, Aggregates, Repositories, events, Application Services, package structure, or integration. Source: `Purpose` (3-17) and the corresponding full sections (37-241).
- Mini primary bias is unchanged: operational DDD rather than renamed CRUD, with explicit context, local language, small invariant boundaries, identity references, and boundary translation. Source: `Purpose` (3-17), `Primary Directive` (21-33), `Aggregate Rules of Thumb` (78-106), `Context Integration Rules` (212-230), `Code Generation Rules` (259-278), `Final Instruction` (328-337).
- Nano activation is unchanged and names context leakage, fake tactical patterns, Aggregate sprawl, and cross-context model coupling as tight-context triggers. Source: strategic anti-patterns (56-60), aggregate anti-patterns (102-106), `Practical Simplicity Rule` (245-255), `Final Instruction` (328-337).
- Nano primary bias is unchanged: local context, language, and invariants take priority over reuse, ORM navigation, object graphs, and framework or client shape. Source: `Bounded Context Is Mandatory` (39-44), `Ubiquitous Language Rules` (64-75), `Aggregate Rules of Thumb` (78-106), `Primary Directive` (21-33), `Client Representation and Scope Discipline` (234-241).

## Mini mapping

Decision rules:

- `M1` Name the Bounded Context before interpreting model artifacts and reject a global company model. Source: `Purpose` (3-17), `Primary Directive` (21-33), `Bounded Context Is Mandatory` (39-44), `Code Generation Rules` (259-278), `Final Instruction` (328-337).
- `M2` Use one local Ubiquitous Language consistently across implementation artifacts and rename code when understanding improves. Source: `Purpose` (8-15), `Primary Directive` (25-33), `Ubiquitous Language Rules` (64-75), `Domain and Transformation Service Rules` (130-139), `Code Generation Rules` (259-270), `Review Checklist` (310-324), `Final Instruction` (328-337).
- `M3` Protect the Core Domain, spend rich modeling only where complexity warrants it, keep supporting or CRUD areas simpler, and avoid DDD ceremony. Source: `Core Domain Protection` (51-55), `Practical Simplicity Rule` (245-255).
- `M4` Make context interactions explicit through visible relationships, translation responsibility, and upstream/downstream influence; prevent external, partner, or legacy models from defining the local model, and avoid sharing model classes across contexts by default. Source: `Bounded Context Is Mandatory` (39-44), `Context Mapping Is a Design Artifact` (45-50).
- `M5` Use an Anticorruption Layer for legacy systems or foreign models, translating their language while keeping foreign schemas and statuses out of local domain objects and owning the translation explicitly. Source: `Context Mapping Is a Design Artifact` (45-50), `Anticorruption Layer` (214-220).
- `M6` Treat Aggregates as small immediate consistency boundaries; expose only the root externally, route invariant-changing operations through it, prevent external mutation of internals, and expose intention-revealing behavior. Source: `Aggregates Are Consistency Boundaries` (80-84), `Aggregate Root Discipline` (86-90), aggregate anti-patterns (102-106), `Code Generation Rules` (259-278), `Review Rules` (282-294).
- `M7` Reference other Aggregates by identity, avoid graph loading by default, and modify one Aggregate per transaction unless there is a compelling reason not to, using eventual events, policies, or process coordination where appropriate. Source: `Primary Directive` (21-33), `Reference Other Aggregates by Identity` (92-96), `One Aggregate per Transaction by Default` (97-100), aggregate anti-patterns (102-106), `Domain Event Rules` (159-165), `Final Instruction` (328-337).
- `M8` Use Entities where identity and lifecycle matter; require meaningful state transitions and domain behavior, and prohibit passive ORM containers in behavior-rich domains. Source: `Entities` (112-117).
- `M9` Use Value Objects aggressively where primitives hide meaning; make them immutable by default, validate on construction, compare by value, model meaningful local values explicitly, and keep invariant enforcement near the concept. Source: `Value Objects` (118-123), required behavior (124-126).
- `M10` Use a Domain Service only for a domain-significant operation requiring multiple domain objects that fits no single Entity or Value Object; name it in the Ubiquitous Language and do not use services to avoid modeling. Use a Transformation Service when domain information must be transformed without assigning behavior to the wrong object, while keeping technical mapping outside the domain and out of domain-sounding services. Source: `Domain and Transformation Service Rules` (130-139).
- `M11` Provide Repositories for Aggregate Roots; define domain- or application-owned interfaces that reconstitute and persist Aggregates, return domain objects or results rather than ORM rows, and exclude business rules. Repository APIs should reflect Aggregate access needs rather than generic table CRUD. Source: `Repository Rules` (143-155).
- `M12` Publish Domain Events for meaningful business facts with past-tense names and model-local payloads; use them for eventual cross-boundary coordination, not every property change, transport mechanics, or missing Aggregate design. Source: `Domain Event Rules` (159-166), event anti-patterns (174-178), `Review Rules` (282-294), `Review Checklist` (310-324).
- `M13` Use Event Sourcing only when the event sequence is the right persistence model, with Aggregate identity, versioning, deterministic replay, and evolution support; Domain Events alone do not justify it. Source: `Event Sourcing` (167-172).
- `M14` Keep Application Services as thin use-case coordinators that load Aggregates, invoke domain behavior, persist, and publish resulting events; they may own transaction boundaries and integration coordination but must not contain core decision logic. Source: `Application Service Rules` (182-193).
- `M15` Organize modules by Bounded Context first and by domain or use-case ownership inside the context; avoid giant shared or common domain packages and keep the model visible in the structure. Source: `Module and Package Rules` (197-208), strategic anti-patterns (56-60).
- `M16` Use DTOs, projections, queries, rendition adapters, mediators, and application-facing representations when client needs differ from Aggregate shape; tailor them without reshaping the Domain Model, compose contexts at application or integration boundaries, separate commands and queries when justified, and keep scope identifiers explicit where context or ownership affects invariants or access. Source: `Client Representation and Scope Discipline` (234-241).
- `M17` Follow the source code-generation order from context and language through tactical classification, a conservative Aggregate boundary, identity references, local invariants, Aggregate-oriented Repositories, use-case Application Services, and context or infrastructure translation. Source: `Code Generation Rules` (259-278).
- `M18` Test domain behavior and boundaries directly, including Aggregate invariants, transitions, Value Objects, events, Repository infrastructure, translation layers, and Application Service orchestration. Source: `Testing Rules` (298-306).

Trigger rules:

- `M19` A term carrying multiple meanings locally, changing meaning across contexts, or remaining a technical placeholder triggers use of the context-local business term and renaming when understanding improves; no split, qualification, or pre-coding artifact is prescribed. Source: `Bounded Context Is Mandatory` (39-44), `Ubiquitous Language Rules` (64-75).
- `M20` Direct imports of another context's domain package, enums shared across contexts with different semantics, or direct database coupling trigger explicit identifiers, integration messages, and separate contract models instead. Source: strategic anti-patterns (56-60), `Identity Across Contexts` (222-225), context-integration anti-patterns (227-230), `Review Checklist` (310-324).
- `M21` A legacy system or foreign model defining local domain code triggers an Anticorruption Layer; API, transport, persistence, infrastructure, or client shape triggers an application-facing representation or technical mapping boundary instead. Source: `Primary Directive` (21-33), `Context Mapping Is a Design Artifact` (45-50), `Domain and Transformation Service Rules` (130-139), `Anticorruption Layer` (214-220), `Client Representation and Scope Discipline` (234-241).
- `M22` An Aggregate boundary change triggers centering on invariants that must hold immediately; a multi-Aggregate transaction requires a compelling reason rather than convenience, with events, policies, or process coordination when consistency can be eventual. Source: `Aggregates Are Consistency Boundaries` (80-84), `One Aggregate per Transaction by Default` (97-100).
- `M23` External mutation of Aggregate internals or an invariant-changing operation outside the root triggers movement behind intention-revealing root behavior. Source: `Aggregate Root Discipline` (86-90), aggregate anti-patterns (102-106), `Review Rules` (282-294).
- `M24` A giant generic Repository abstraction or a Repository per table without Aggregate thinking triggers replacement of that prohibited design; ORM-row or persistence-entity returns trigger domain objects or domain-oriented results, and rule-owning implementations trigger moving business rules back to the model. Repository APIs should reflect Aggregate access needs rather than generic table CRUD. Source: `Repository Rules` (143-155), `Code Generation Rules` (259-278), `Review Rules` (282-294).
- `M25` Events emitted for every property change, named as commands, or carrying framework request objects or persistence artifacts trigger restoration of meaningful business facts through past-tense fact names and model-local payloads. Source: `Domain Event Rules` (159-166), event anti-patterns (174-178), `Review Rules` (282-294), `Review Checklist` (310-324).
- `M26` The Domain Model's core decision logic or all branching business rules in Application Services trigger movement into the qualifying domain object or Domain Service; duplicated controller orchestration returns to the Application Service. Source: `Domain and Transformation Service Rules` (130-139), `Application Service Rules` (182-193).
- `M27` Client rendering, query speed, or representation pressure triggers DTOs, projections, use-case queries, or adapters instead of exposing or reshaping Aggregates. Source: `Client Representation and Scope Discipline` (234-241).
- `M28` Simple CRUD subdomains trigger simpler patterns, while real invariants and lifecycle complexity trigger honest modeling. Source: `Practical Simplicity Rule` (245-255).

Final checklist:

- The checklist restates `M1`-`M16`, `M18`, and `M20`-`M27` as a final scan rather than introducing new rules; `M17` remains an execution-order rule and `M28` is represented through the Core Domain/simplicity check. Source: `Review Checklist` (310-324), `Testing Rules` (298-306), `Final Instruction` (328-337).

## Nano mapping

Decision rules:

- `N1` Name the Bounded Context and local Ubiquitous Language before interpreting model artifacts. Source: `Purpose` (8-15), `Primary Directive` (21-33), `Bounded Context Is Mandatory` (39-44), `Ubiquitous Language Rules` (64-75).
- `N2` Across Bounded Contexts, use explicit identifiers and integration messages, keep contract models separate, do not pass local Aggregates, avoid sharing model classes by default, and prohibit shared enums when semantics differ. Source: `Bounded Context Is Mandatory` (39-44), strategic anti-patterns (56-60), `Identity Across Contexts` (222-225), context-integration anti-patterns (227-230).
- `N3` Treat Aggregates as small immediate consistency boundaries; route invariant-changing operations through the root, prevent external mutation, reference other Aggregates by identity, and keep cross-Aggregate coordination usually eventual. Source: `Aggregate Rules of Thumb` (78-100), aggregate anti-patterns (102-106), `Final Instruction` (328-337).
- `N4` Use Entities where identity and lifecycle matter, rejecting passive ORM containers in behavior-rich domains; make Value Objects immutable by default and validated at construction; use a Domain Service only for a domain-significant operation requiring multiple objects that fits no Entity or Value Object. Source: `Entity and Value Object Rules` (110-126), `Domain and Transformation Service Rules` (130-139).
- `N5` Keep Repositories focused on reconstituting and persisting Aggregate Roots and Application Services focused on coordinating use cases rather than making the Domain Model's core decisions; Application Services may own transaction boundaries and integration coordination. Source: `Repository Rules` (143-155), `Application Service Rules` (182-193).
- `N6` Publish Domain Events only for meaningful business facts with past-tense names and use Event Sourcing only when the event sequence is the right persistence model. Source: `Domain Event Rules` (159-166), `Event Sourcing` (167-172), event anti-patterns (174-178).
- `N7` Use client representations, projections, queries, or adapters when client needs differ from Aggregate shape instead of exposing or reshaping domain internals; keep scope identifiers explicit where context or ownership affects invariants or access. Source: `Client Representation and Scope Discipline` (234-241).

Trigger rules:

- `N8` A term carrying multiple meanings locally, changing meaning across contexts, or remaining a technical placeholder triggers use of the context-local business term and renaming when understanding improves; no split, qualification, or pre-coding artifact is prescribed. Source: `Bounded Context Is Mandatory` (39-44), `Ubiquitous Language Rules` (64-75).
- `N9` A multi-Aggregate transaction requires a compelling reason rather than convenience; boundaries remain centered on immediate invariants, references use identities, and events, policies, or process coordination handle eventual consistency. Source: `Aggregates Are Consistency Boundaries` (80-84), `Reference Other Aggregates by Identity` (92-96), `One Aggregate per Transaction by Default` (97-100).
- `N10` Legacy or foreign models entering local domain code trigger an Anticorruption Layer; database, framework, transport, infrastructure, or client pressure triggers a technical mapping or application-facing representation at the boundary. Source: `Primary Directive` (21-33), `Domain and Transformation Service Rules` (130-139), `Anticorruption Layer` (214-220), `Client Representation and Scope Discipline` (234-241).
- `N11` DDD vocabulary around CRUD services, generic Repositories, mutable graphs, or anemic models triggers either honest modeling of real invariants and behavior or use of a simpler pattern; no proof artifact is required. Source: `Primary Directive` (21-33), `Repository Rules` (143-155), `Practical Simplicity Rule` (245-255), `Final Instruction` (328-337).
- `N12` DDD review triggers checks for context, language, Aggregate boundary, translation, Repository shape, events-as-facts, and Application Service thinness. Source: `Review Rules` (282-294), `Review Checklist` (310-324).

Final checklist:

- The checklist restates `N1`-`N7`, `N9`, `N10`, and `N12` as a final scan rather than introducing new rules; `N8` and `N11` remain trigger-only reminders.

## Section coverage review

- `Purpose` operational priorities (3-15): covered by `M1`, `M2`, `M4`, `M6`, `M7`, `M15`, `N1`, `N2`, and `N3`; practical implementation rather than theory theater is covered by `M3`, `M28`, and `N11`.
- `Purpose` policy modality (17): covered by the binding wording retained in `M*` and `N*` rules; every retained mechanism preserves its source modality, and intentional nano mechanism losses are identified below.
- `Primary Directive` uncertainty order (21-31): covered by `M17`; the ordered procedure is intentionally lost from nano, while its high-salience context, language, Aggregate, identity, infrastructure, and translation decisions are covered by `N1`-`N3`, `N7`, and `N10`.
- `Primary Directive` rejection of renamed CRUD (33): covered by `M28` and `N11`.
- `Bounded Context Is Mandatory` (39-43): covered by `M1`, `M4`, `N1`, and `N2`; model-class sharing retains the source's `by default` qualifier.
- `Context Mapping Is a Design Artifact` (45-49): covered by `M4`, `M5`, `M20`, `M21`, `N2`, and `N10`; relationship, responsibility, influence, and local-model protection remain distinct.
- `Core Domain Protection` (51-54): covered by `M3`; nano intentionally loses the Core/supporting-subdomain allocation detail.
- Strategic anti-patterns (56-60): covered by `M1`, `M4`, `M15`, `M20`, `N2`, and `N12`; the global model, shared package, diagram-only boundary, and direct-import effects all survive.
- `Ubiquitous Language Rules` term semantics and rename rule (64-70): covered by `M2`, `M19`, `N1`, and `N8`; split, qualification, and before-coding mechanisms are not claimed because the source does not prescribe them.
- `Ubiquitous Language Rules` required naming behavior (72-74): covered by `M2`, `M19`, and `N8`.
- `Aggregates Are Consistency Boundaries` (80-84): covered by `M6`, `M22`, `N3`, and `N9`; boundary choice remains centered on invariants that must hold immediately, without a proof or list artifact.
- `Aggregate Root Discipline` (86-90): covered by `M6`, `M23`, and `N3`; root routing is scoped to invariant-changing operations and external mutation of internals.
- `Reference Other Aggregates by Identity` (92-95): covered by `M7`, `N3`, and `N9`.
- `One Aggregate per Transaction by Default` (97-100): covered by `M7`, `M22`, `N3`, and `N9`; the compelling-reason exception and anti-convenience condition are retained.
- Aggregate anti-patterns (102-106): covered by `M6`, `M7`, `M22`, `M23`, `N3`, `N9`, and `N11`; ORM navigation, default multi-Aggregate transactions, mutable children, and direct navigation are merged into boundary, root, identity, and honesty rules.
- `Entities` (112-116): covered by `M8` and `N4`; the passive-container prohibition and checklist behavior-bearing check remain qualified to behavior-rich domains.
- `Value Objects` (118-122): covered by `M9`; `N4` retains only immutability `by default` and construction validation. The primitive-hiding selection condition and equality-by-value are intentionally lost from nano.
- Value Object required behavior (124-126): covered by `M9`; the meaningful/descriptive-value selection condition, identifier/quantity/range/name examples, and near-concept invariant enforcement are intentionally lost from nano.
- Domain Service rules (132-133): covered by `M10` and `N4`; all three predicates survive in decision rules and both final checklists: a domain-significant operation, multiple domain objects, and no fitting Entity or Value Object.
- Transformation Service and technical-mapping rules (134-135): covered by `M10`; the Transformation Service mechanism is intentionally lost from nano, while its keep-technical-mapping-outside-the-domain effect is covered by `N10`.
- Domain and Transformation Service anti-patterns (137-139): covered by `M10`, `M26`, `N4`, `N10`, and `N11`; service extraction cannot replace object modeling or disguise technical mapping.
- Repository core rules (145-149): covered by `M11`; `N5` retains only Aggregate Root focus plus reconstitution and persistence semantics in its decision rule and final checklist. `M11` preserves the Aggregate-access API recommendation as `should`; interface ownership, that recommendation, and the result-form rule are intentionally lost from nano.
- Repository anti-patterns (151-155): covered by `M11` and `M24`; `N11` retains only the generic-Repository DDD-theater pressure. Giant generic, rule-owning, and persistence-entity-returning effects remain prohibited in mini, and repository-per-table design retains the source qualifier `without Aggregate thinking`. Table-shaped design alone is not claimed as a mandatory reshape trigger; the specific per-table, rule-owning, and persistence-entity anti-patterns are intentionally lost from nano.
- Domain Event core rules (161-165): covered by `M12`, `M22`, `N6`, and `N12`; events remain meaningful business facts with past-tense names, model-local payloads, and eventual-coordination scope.
- `Event Sourcing` (167-172): covered by `M13` and `N6`; nano intentionally loses stream identity/versioning, deterministic replay, and evolution mechanisms while retaining the persistence-model gate.
- Domain Event anti-patterns (174-178): covered by `M12`, `M25`, `N6`, `N10`, and `N12`; `every property change` is retained exactly and remediation returns to meaningful business facts rather than invented rename/narrow/remove steps.
- Application Service core rules (184-188): covered by `M14` and `N5`; transaction-boundary and integration-coordination ownership retains the source's permission, `may own`, rather than becoming mandatory.
- Application Service anti-patterns (190-193): covered by `M11`, `M14`, `M24`, `M26`, `N5`, and `N12`; core decision logic, the `all branching business rules` qualifier, duplicated controller orchestration, and Repository/Application Service invariant duplication are retained, while permitted transaction-boundary and integration coordination remain covered by `M14` and `N5`. Nano contains no unqualified branching-removal trigger, so no nano wording changes.
- Module and package rules (199-202): covered by `M15`, with Bounded Context visibility also reinforced by `M1` and `N1`; nano intentionally loses the within-context domain/use-case organization detail.
- Preferred package examples (204-208): intentionally lost as literal examples; their context-first, domain/application/infrastructure/interfaces organization effect is covered by `M15`.
- `Anticorruption Layer` (214-220): covered by `M5`, `M21`, and `N10`; ACL use remains specific to legacy systems or foreign models.
- `Identity Across Contexts` (222-225): covered by `M4`, `M20`, and `N2`; identifiers, integration messages, no direct Aggregate passing, and contract-model separation remain explicit.
- Context-integration anti-patterns (227-230): covered by `M20` and `N2`; enum sharing is prohibited only when semantics differ, while direct imports and database coupling remain unqualified prohibitions.
- `Client Representation and Scope Discipline` (234-241): covered by `M16`, `M21`, `M27`, `N7`, and `N10`; client representations remain conditional on client needs differing from Aggregate shape, scope identifiers remain conditional on context or ownership affecting invariants or access, and both remain distinct from ACLs and technical infrastructure mappings.
- `Practical Simplicity Rule` (247-250): covered by `M3`, `M28`, and `N11`.
- Practical-simplicity anti-patterns (252-255): covered by `M3`, `M28`, and `N11`; over-modeling and under-modeling are preserved without requiring a proof artifact.
- Code-generation order (261-270): covered by `M17`; the order is intentionally lost from nano, with its high-salience decisions covered individually by `N1`-`N7` and `N10`.
- Code-generation avoid-by-default list (272-278): covered by `M4`, `M6`, `M7`, `M11`, `M14`, `M15`, `M20`, `M22`, `M24`, `M26`, `N2`, `N3`, `N5`, `N9`, and `N11`.
- `Review Rules` (282-294): covered by `M1`, `M4`-`M7`, `M11`, `M12`, `M19`-`M25`, `N1`-`N3`, and `N8`-`N12`; each listed smell is merged into a corresponding decision or trigger.
- `Testing Rules` (298-306): covered by `M18`; testing detail is intentionally lost from nano.
- `Review Checklist` (310-324): covered by the mini and nano final checklists and by `M1`, `M2`, `M4`, `M6`, `M7`, `M11`, `M12`, `M14`, `M20`, `M22`-`M26`, `N1`-`N3`, `N5`, `N6`, `N9`, `N10`, and `N12`.
- `Final Instruction` (328-337): covered by `M1`, `M2`, `M4`, `M5`, `M7`, `M22`, `M28`, `N1`-`N3`, and `N9`-`N11`; no final-instruction rule is intentionally lost.
