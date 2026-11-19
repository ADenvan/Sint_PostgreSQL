
## Базовый синтаксис HAVING

Обычно запрос с `HAVING` выглядит так:

```sql
SELECT
  group_column,
  aggregate_function(column) AS result
FROM table_name
WHERE row_condition
GROUP BY group_column
HAVING group_condition
ORDER BY result;
```

Например:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING COUNT(*) > 100;
```

Этот запрос читается так:

> Сгруппируй пользователей по стране и покажи только те страны, где пользователей больше 100.

Результат может быть таким:

|country|users_count|
|---|--:|
|RU|240|
|BR|180|
|DE|126|

Страны, где пользователей 100 или меньше, в результат не попадут.