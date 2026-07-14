Review the following design and recommend a better module boundary.

```text
OrderController
  -> OrderService.create(request, validateOnly)
     -> OrderValidator.validate(request)
     -> OrderMapper.toRow(request)
     -> OrderRepository.insert(row)
        -> SqlOrderGateway.executeInsert(row)
           -> DatabaseClient.query(sql, params)
```

`OrderService` mostly forwards arguments. `OrderRepository` and
`SqlOrderGateway` each rename one database operation. The controller must know
that validation happens before mapping, map database duplicate-key errors to a
domain result, and choose `validateOnly=false` for normal writes. Adding a new
required order field currently changes six files.

Explain which boundaries earn their existence, which knowledge should move
behind one interface, and how to reduce the facts an ordinary caller must
coordinate. Do not assume that more layers or smaller files are improvements.
