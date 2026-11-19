
## Когда использовать GROUP BY

Используй `GROUP BY`, когда в задаче звучат слова:

- «по каждому»;
- «по категориям»;
- «по странам»;
- «по месяцам»;
- «сколько всего»;
- «сумма по»;
- «среднее по»;
- «минимум и максимум по»;
- «топ по количеству».

Например:

«Сколько заказов у каждого клиента?» — почти точно нужен `GROUP BY customer_id`.

```sql
SELECT
  customer_id,
  COUNT(*) AS orders_count
FROM orders
GROUP BY customer_id;
```

«Какая выручка по каждому месяцу?» — нужен `GROUP BY` по месяцу.

```sql
SELECT
  DATE_TRUNC('month', created_at) AS month,
  SUM(amount) AS total_amount
FROM orders
GROUP BY 1
ORDER BY 1;
```

«Какая средняя цена товара в каждой категории?» — нужен `GROUP BY category`.

```sql
SELECT
  category,
  AVG(price) AS avg_price
FROM products
GROUP BY category;
```