
## GROUP BY и SUM

Один из самых частых сценариев — сумма по группам.

Например, нужно посчитать выручку по каждому клиенту:

```sql
SELECT
  customer_id,
  SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id
ORDER BY total_amount DESC;
```

Результат:

|customer_id|total_amount|
|--:|--:|
|101|1300|
|102|800|
|103|200|

Так можно быстро понять, какие клиенты принесли больше всего денег.

---
## GROUP BY и AVG

`AVG` считает среднее значение внутри группы.

Например, средний чек по каждому клиенту:

```sql
SELECT
  customer_id,
  AVG(amount) AS avg_order_amount
FROM orders
GROUP BY customer_id
ORDER BY avg_order_amount DESC;
```

Если у клиента было три заказа на `500`, `700` и `100`, средний чек будет:

```sql
SELECT (500 + 700 + 100) / 3.0 AS avg_amount;
```

Результат:

|avg_amount|
|--:|
|433.3333333333333333|

В реальных отчётах среднее часто округляют:

```sql
SELECT
  customer_id,
  ROUND(AVG(amount), 2) AS avg_order_amount
FROM orders
GROUP BY customer_id
ORDER BY avg_order_amount DESC;
```