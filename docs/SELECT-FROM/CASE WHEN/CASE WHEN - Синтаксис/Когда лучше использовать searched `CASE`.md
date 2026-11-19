
## Когда лучше использовать searched `CASE`

Searched `CASE` гибче.
Например, нужно определить тип заказа по сумме и статусу:

```sql
SELECT
  id,
  amount,
  status,
  CASE
    WHEN status = 'cancelled' THEN 'cancelled'
    WHEN amount >= 10000 THEN 'large_paid_order'
    WHEN amount >= 1000 THEN 'regular_paid_order'
    ELSE 'small_paid_order'
  END AS order_type
FROM orders
WHERE status IN ('paid', 'cancelled');
```

Здесь мы проверяем не просто одно значение. У нас есть разные условия: статус, сумма, порядок правил.

Для таких случаев searched `CASE` читается лучше и даёт больше контроля.