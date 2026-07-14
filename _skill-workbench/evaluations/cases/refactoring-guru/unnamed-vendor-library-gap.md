# Missing Operations On A Vendor Type

We use `@vendor/billing-date`. The package is externally maintained, and we cannot change its `BillingDate` class.

Today one call site needs this operation:

```ts
function nextChargeDate(date: BillingDate, holidays: HolidayCalendar): BillingDate {
  let candidate = date.plusDays(1);
  while (candidate.isWeekend() || holidays.contains(candidate)) {
    candidate = candidate.plusDays(1);
  }
  return candidate;
}
```

A roadmap document mentions possible future operations such as grace-period calculation, statement-cycle alignment, and collection-window checks, but none is approved and no other call site needs them yet. The team is debating:

- one local helper near this use,
- a wrapper around every `BillingDate`,
- a local extension type containing the current and possible future operations,
- or a fork of the package.

Choose the smallest justified structure now. State what concrete evidence would justify moving to a more substantial local extension later, how callers should migrate, and what compatibility checks matter when the vendor package changes.
