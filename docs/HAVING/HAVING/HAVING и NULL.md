
## HAVING и NULL

Агрегатные функции по-разному относятся к `NULL`.

`COUNT(*)` считает строки даже с `NULL`.

`COUNT(column)` игнорирует `NULL`.

`SUM(column)` и `AVG(column)` тоже игнорируют `NULL`.

Например, есть таблица `orders`:

|id|customer_id|amount|
|--:|--:|--:|
|1|1|100|
|2|1|NULL|
|3|1|200|
|4|2|NULL|

Запрос:

```sql
SELECT
  customer_id,
  COUNT(*) AS rows_count,
  COUNT(amount) AS paid_orders_count,
  SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id;
```

Результат:

|customer_id|rows_count|paid_orders_count|total_amount|
|--:|--:|--:|--:|
|1|3|2|300|
|2|1|0|NULL|

У клиента `2` сумма получилась `NULL`, потому что у него нет ни одного ненулевого значения `amount`.

Если написать:

```sql
SELECT
  customer_id,
  SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 100;
```

клиент `2` не попадёт в результат: сравнение `NULL > 100` не даёт `TRUE`.

Если хочешь считать пустую сумму как ноль, можно использовать `COALESCE`:
^h1
```sql
SELECT
  customer_id,
  COALESCE(SUM(amount), 0) AS total_amount
FROM orders
GROUP BY customer_id
HAVING COALESCE(SUM(amount), 0) > 100;
```

^7894cb
