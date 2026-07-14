# Resolve a Two-Axis Inheritance Refactoring

Focused tests protect all current behavior. A report hierarchy mixes two independent variation axes:

- output format: PDF or HTML
- delivery mode: download or scheduled email

The current subclasses are `PdfDownloadReport`, `PdfEmailReport`, `HtmlDownloadReport`, and `HtmlEmailReport`. Every new format requires two subclasses, and every new delivery mode requires one subclass per format.

Two reviewers dispute whether the catalog's Tease Apart Inheritance move applies or whether the hierarchy should merely be collapsed. Resolve that exact source interpretation. State the applicability condition, the smallest behavior-preserving sequence, verification points, and the stopping condition. Do not add new behavior or perform a complete refactoring audit.
