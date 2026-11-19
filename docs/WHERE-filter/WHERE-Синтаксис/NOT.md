
## NOT: отрицание условия
`NOT` переворачивает условие.

Например, найти заказы, которые не отменены:

```sql
SELECT id, status, amount
FROM orders
WHERE NOT status = 'cancelled';
```

То же самое обычно пишут проще:

```sql
SELECT id, status, amount
FROM orders
WHERE status <> 'cancelled';
```

Ещё пример: найти товары, которых нет в наличии.

```sql
SELECT id, name, in_stock
FROM products
WHERE NOT in_stock;
```

Такой запрос удобен, если `in_stock` — булева колонка со значениями `TRUE` или `FALSE`.