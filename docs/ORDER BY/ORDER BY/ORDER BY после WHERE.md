
## ORDER BY после WHERE

`ORDER BY` выполняется после фильтрации.

Например, нужно взять только оплаченные заказы и отсортировать их от новых к старым:

```sql
SELECT id, customer_id, amount, created_at
FROM orders
WHERE status = 'paid'
ORDER BY created_at DESC;
```

Сначала `WHERE` оставит только оплаченные заказы. Потом `ORDER BY` отсортирует уже отфильтрованный результат.

Порядок частей запроса важен:

```sql
SELECT columns
FROM table_name
WHERE condition
ORDER BY column_name;
```

Нельзя поставить `ORDER BY` перед `WHERE` или `FROM`. SQL ожидает части запроса в своём порядке.