
## EXISTS в SELECT

`EXISTS` можно использовать не только в `WHERE`, но и в списке колонок `SELECT`.

Например, мы хотим вывести всех клиентов и рядом показать флаг: есть у клиента заказы или нет.

```sql
SELECT
  c.id,
  c.name,
  EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.id
  ) AS has_orders
FROM customers c;
```

Результат:

|id|name|has_orders|
|--:|---|---|
|1|Anna|true|
|2|Bob|false|
|3|Vera|true|
|4|Gleb|false|

Это удобно для отчётов, админок и API, когда нужно не отфильтровать строки, а добавить к каждой строке признак.

Например:

- `has_orders`;
- `has_comments`;
- `has_active_subscription`;
- `has_unread_messages`.