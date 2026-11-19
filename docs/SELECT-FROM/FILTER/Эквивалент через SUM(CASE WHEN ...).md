
## Эквивалент через SUM(CASE WHEN ...)

Важно понимать, что `FILTER` не делает что-то принципиально невозможное без него.

Многие запросы можно переписать через `CASE`.

Например:

```sql
SELECT
  COUNT(*) FILTER (WHERE status = 'paid') AS paid_orders
FROM orders;
```

Можно записать так:

```sql
SELECT
  SUM(CASE WHEN status = 'paid' THEN 1 ELSE 0 END) AS paid_orders
FROM orders;
```

Оба запроса посчитают количество оплаченных заказов.

Выручка через `FILTER`:

```sql
SELECT
  SUM(amount) FILTER (WHERE status = 'paid') AS revenue_paid
FROM orders;
```

То же самое через `CASE`:

```sql
SELECT
  SUM(CASE WHEN status = 'paid' THEN amount ELSE 0 END) AS revenue_paid
FROM orders;
```

`CASE` полезен, потому что работает почти во всех СУБД.

А `FILTER` полезен, потому что делает запрос чище, если ваша база его поддерживает.