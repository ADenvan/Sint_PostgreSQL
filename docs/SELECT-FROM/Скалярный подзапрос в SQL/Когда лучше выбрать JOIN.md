
## Когда лучше выбрать JOIN

Скалярный подзапрос хорош, когда нужно получить **одно дополнительное значение**.

Например:

```sql
SELECT
  c.id,
  c.name,
  (
    SELECT COUNT(*)
    FROM orders o
    WHERE o.customer_id = c.id
  ) AS orders_count
FROM customers c;
```

Но если ты начинаешь добавлять три, четыре, пять подзапросов подряд, это уже тревожный сигнал.

Например:

```sql
SELECT
  c.id,
  c.name,
  (
    SELECT COUNT(*)
    FROM orders o
    WHERE o.customer_id = c.id
  ) AS orders_count,
  (
    SELECT SUM(o.amount)
    FROM orders o
    WHERE o.customer_id = c.id
  ) AS total_spent,
  (
    SELECT MAX(o.created_at)
    FROM orders o
    WHERE o.customer_id = c.id
  ) AS last_order_at
FROM customers c;
```

Такой запрос уже хочется переписать через `JOIN` и агрегацию:

```sql
SELECT
  c.id,
  c.name,
  COUNT(o.id) AS orders_count,
  COALESCE(SUM(o.amount), 0) AS total_spent,
  MAX(o.created_at) AS last_order_at
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY c.id, c.name;
```

И читается цельнее, и база обычно работает увереннее.