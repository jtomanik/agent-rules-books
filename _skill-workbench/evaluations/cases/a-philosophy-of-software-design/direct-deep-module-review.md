Use A Philosophy of Software Design to review this proposed export pipeline.

The API exposes `prepareExport(options)`, `loadRows(handle)`,
`normalizeRows(handle, mode)`, `writeArchive(handle, format)`, and
`finalizeExport(handle)`. Callers must retain the handle, invoke the methods in
order, select a normalization mode that matches the requested format, and
delete a temporary directory if any step fails. Three handlers repeat this
sequence with slightly different error cleanup.

Decide whether the module and API are deep enough, identify information that
should be hidden, and propose the public contract and ownership boundary. Keep
the review focused on design judgment rather than implementation syntax.
