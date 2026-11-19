## Как читать EXISTS-запрос

Возьмём запрос:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
    AND o.status = 'paid'
);
```

Его можно прочитать так:

> Верни клиентов, для которых существует хотя бы один заказ со статусом `paid`.

А такой запрос:

```sql
SELECT *
FROM products p
WHERE NOT EXISTS (
  SELECT 1
  FROM order_items oi
  WHERE oi.product_id = p.id
);
```

читается так:

> Верни товары, для которых не существует ни одной строки в позициях заказов.

Если вы можете перевести запрос с `EXISTS` на обычный язык, значит, вы понимаете его правильно.