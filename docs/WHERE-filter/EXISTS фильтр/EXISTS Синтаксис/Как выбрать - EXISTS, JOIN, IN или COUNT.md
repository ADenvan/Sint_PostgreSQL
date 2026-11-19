
## Как выбрать: EXISTS, JOIN, IN или COUNT

Короткая шпаргалка:

|Задача|Что выбрать|
|---|---|
|Нужны клиенты, у которых есть заказы|`EXISTS`|
|Нужны клиенты, у которых нет заказов|`NOT EXISTS`|
|Нужны клиенты вместе с данными заказов|`JOIN`|
|Нужно проверить значение в коротком списке|`IN`|
|Нужно посчитать количество заказов|`COUNT`|
|Нужно добавить флаг «есть заказы»|`EXISTS` в `SELECT`|
|Нужно найти отсутствующие связи|`NOT EXISTS`|

Примеры.

Клиенты с заказами:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

Клиенты без заказов:

```sql
SELECT *
FROM customers c
WHERE NOT EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

Клиенты и их заказы:

```sql
SELECT
  c.id,
  c.name,
  o.id AS order_id,
  o.amount
FROM customers c
JOIN orders o ON o.customer_id = c.id;
```

Количество заказов по клиентам:

```sql
SELECT
  c.id,
  c.name,
  COUNT(o.id) AS orders_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY c.id, c.name;
```