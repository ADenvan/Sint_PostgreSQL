
## EXISTS с UPDATE

`EXISTS` можно использовать не только в `SELECT`, но и в других командах, например в `UPDATE`.

Допустим, нужно пометить клиентов как активных, если у них есть оплаченный заказ.

```sql
UPDATE customers c
SET is_active = TRUE
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
    AND o.status = 'paid'
);
```

Логика такая:

> Обнови только тех клиентов, для которых существует оплаченный заказ.

Это удобный способ обновлять строки на основе связанных данных.