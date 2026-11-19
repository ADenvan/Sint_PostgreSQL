
## HAVING и DISTINCT

Иногда перед `HAVING` внутри агрегата используют `DISTINCT`.

Например, нужно найти пользователей, которые покупали товары минимум из 3 разных категорий.

Допустим, есть таблица `orders`:

|id|customer_id|category|
|--:|--:|---|
|1|1|books|
|2|1|books|
|3|1|games|
|4|1|courses|
|5|2|books|
|6|2|books|

Запрос:

```sql
SELECT
  customer_id,
  COUNT(DISTINCT category) AS categories_count
FROM orders
GROUP BY customer_id
HAVING COUNT(DISTINCT category) >= 3;
```

Результат:

|customer_id|categories_count|
|--:|--:|
|1|3|

Клиент `1` покупал в трёх разных категориях: `books`, `games`, `courses`.

Клиент `2` покупал только в одной категории, поэтому не прошёл условие.