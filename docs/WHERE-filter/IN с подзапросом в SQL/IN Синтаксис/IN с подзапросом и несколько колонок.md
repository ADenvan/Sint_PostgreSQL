
## IN с подзапросом и несколько колонок

Обычный `IN` сравнивает одно значение с одним списком.

```sql
WHERE customer_id IN (
  SELECT id
  FROM customers
)
```

Иногда нужно сравнить пару значений. В PostgreSQL можно использовать такую форму:

```sql
SELECT *
FROM order_items
WHERE (order_id, product_id) IN (
  SELECT order_id, product_id
  FROM returned_items
);
```

Здесь сравнивается пара `order_id` + `product_id`.

Но такая запись хуже переносится между разными базами данных и может быть непривычной для новичков.

Часто понятнее написать через `EXISTS`:

```sql
SELECT *
FROM order_items oi
WHERE EXISTS (
  SELECT 1
  FROM returned_items ri
  WHERE ri.order_id = oi.order_id
    AND ri.product_id = oi.product_id
);
```

Так явно видно, какие колонки с какими сравниваются.