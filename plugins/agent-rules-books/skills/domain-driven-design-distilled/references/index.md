# Domain-Driven Design Distilled Reference Index

Use `SKILL.md` alone when it resolves ordinary matched work. For an explicit dispute, demonstrated modeling hotspot, or one bounded source question left unresolved after applying the skill, use the table to select the smallest relevant sections of [full.md](full.md). For a complete DDD Distilled audit or a decision spanning several independent concern families, read [full.md](full.md) end to end.

| Section | Lines | Read when |
| --- | ---: | --- |
| [Purpose](full.md#purpose) | `3-18` | Decide whether the smallest effective set of DDD practices, business meaning, explicit contexts, Core Domain focus, and practical delivery are the governing lens. |
| [Primary Directive](full.md#primary-directive) | `20-36` | Resolve a dispute about the capability-to-context sequence, whether tactical patterns earn their cost, or whether a proposal has fallen into no modeling or full-ceremony extremes. |
| [Adoption Fit and Modeling Investment](full.md#adoption-fit-and-modeling-investment) | `38-46` | Decide whether domain complexity, language ambiguity, differentiation, or integration risk justifies DDD effort and where reassessment or business-behavior validation is needed. |
| [Strategic Rules](full.md#strategic-rules) | `48-78` | Classify Core, Supporting, and Generic Subdomains; define Bounded Context ownership; or decide where context mapping and translation are required. |
| [Context Relationship Rules](full.md#context-relationship-rules) | `80-99` | Choose a relationship from team coordination, governance, upstream influence, translation cost, protocol needs, interchange language, or integration value. |
| [Integration Style Rules](full.md#integration-style-rules) | `101-110` | Choose among RPC, REST, or messaging, decide event payload versus query-back, or settle contract separation and translation testing. |
| [Ubiquitous Language Rules](full.md#ubiquitous-language-rules) | `112-125` | Resolve overloaded or imported terms, inconsistent names, technical placeholders, or helpers and utilities that conceal domain decisions. |
| [Tactical Pattern Rules](full.md#tactical-pattern-rules) | `127-160` | Decide whether identity, value meaning, invariants, or meaningful facts justify Entities, Value Objects, Aggregates, or Domain Events and their modalities. |
| [Aggregate Minimalism Rules](full.md#aggregate-minimalism-rules) | `162-175` | Review Aggregate size, invariant boundaries, identity references, eventual consistency, transaction scope, whole-graph loading, or exposed mutable children. |
| [Application Service Rules](full.md#application-service-rules) | `177-189` | Separate use-case coordination from domain decisions when services, controllers, or transport shape are taking over the model. |
| [Architecture and Infrastructure Rules](full.md#architecture-and-infrastructure-rules) | `191-203` | Isolate framework, persistence, REST, transport, or integration representations that are defining or leaking into the domain model. |
| [Collaboration Rules](full.md#collaboration-rules) | `205-217` | Resolve a fuzzy business concept through explicit names, tests, events, or model-teaching code, or identify the richer concept concealed by status codes, flags, enums, booleans, or generic helpers. |
| [Practicality Rules](full.md#practicality-rules) | `219-231` | Decide whether simple services and data structures remain honest or rising invariants, lifecycle, and language complexity justify incremental strengthening. |
| [Accelerated Modeling and Project Rules](full.md#accelerated-modeling-and-project-rules) | `233-243` | Select collaborative modeling, timeboxing, spikes, debt tracking, expert involvement, estimation inputs, or ceremony limits for a concrete uncertainty. |
| [Code Generation Rules](full.md#code-generation-rules) | `245-262` | Apply the canonical generation order or review generated code for shared packages, service-centric fake DDD, technical naming, or tactical ceremony. |
| [Review Rules](full.md#review-rules) | `264-279` | Perform a focused review for missing subdomain or context ownership, context bleeding, weak translation, primitive obsession, anemic models, oversized Aggregates, or excess ceremony. |
| [Testing Rules](full.md#testing-rules) | `281-289` | Design tests for Ubiquitous Language, Value Objects, Entity and Aggregate transitions, Application Service orchestration, or context translation. |
| [Review Checklist](full.md#review-checklist) | `291-306` | Run the canonical pre-finalization scan over strategic fit, language, tactical patterns, Aggregate shape, service ownership, infrastructure isolation, and ceremony. |
| [Final Instruction](full.md#final-instruction) | `308-317` | Arbitrate a final uncertain choice by business language, Bounded Context clarity, honest complexity, ceremony cost, and practical delivery. |
