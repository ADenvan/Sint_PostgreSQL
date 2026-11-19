
## Что можно писать в HAVING

В `HAVING` обычно пишут условия на агрегатные функции:

```sql
HAVING COUNT(*) > 10
```

```sql
HAVING SUM(amount) >= 50000
```

```sql
HAVING AVG(rating) >= 4.5
```

```sql
HAVING MIN(price) > 0
```

```sql
HAVING MAX(created_at) >= DATE '2026-01-01'
```

Можно объединять условия через `AND` и `OR`:

```sql
SELECT
  product_id,
  COUNT(*) AS reviews_count,
  AVG(rating) AS avg_rating
FROM reviews
GROUP BY product_id
HAVING COUNT(*) >= 10
   AND AVG(rating) >= 4.0;
```

Такой запрос покажет только товары, у которых есть минимум 10 отзывов и средняя оценка не ниже 4.

Можно использовать диапазоны:

```sql
SELECT
  customer_id,
  SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id
HAVING SUM(amount) BETWEEN 1000 AND 10000;
```

Такой запрос покажет клиентов, у которых сумма заказов от 1000 до 10000 включительно.

Можно использовать `IN`:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING country IN ('RU', 'US', 'DE');
```

Но здесь есть важный нюанс: если условие не использует агрегат, его чаще лучше перенести в `WHERE`.