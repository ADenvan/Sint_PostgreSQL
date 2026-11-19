
## EXISTS vs IN

Ещё один похожий вариант — `IN`.

Клиентов с заказами можно найти так:

```sql
SELECT *
FROM customers
WHERE id IN (
  SELECT customer_id
  FROM orders
);
```

На простых примерах это работает похоже на `EXISTS`.

Запрос с `EXISTS`:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

Запрос с `IN`:

```sql
SELECT *
FROM customers
WHERE id IN (
  SELECT customer_id
  FROM orders
);
```

Оба могут вернуть клиентов, у которых есть заказы.

Но между ними есть различия.

`IN` удобно читать, когда вы проверяете одно значение против списка:

```sql
WHERE status IN ('paid', 'shipped', 'cancelled')
```

А `EXISTS` удобнее, когда нужно проверить наличие строки по условию, особенно если условий несколько:

```sql
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
    AND o.status = 'paid'
    AND o.created_at >= DATE '2026-01-01'
)
```

Кроме того, `EXISTS` часто лучше выражает намерение:

> Мне не нужен список значений. Мне нужно знать, существует ли подходящая строка.