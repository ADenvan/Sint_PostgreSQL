
## GROUP BY и NULL

`NULL` в `GROUP BY` ведёт себя особым образом: все строки с `NULL` в группируемой колонке попадают в одну группу.

Например:

|id|country|
|--:|---|
|1|RU|
|2|NULL|
|3|US|
|4|NULL|
|5|RU|

Запрос:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
ORDER BY country;
```

Результат может быть таким:

|country|users_count|
|---|--:|
|RU|2|
|US|1|
|NULL|2|

То есть `NULL` не исчезает сам по себе. Он образует отдельную группу.

Если не хочешь видеть пользователей без страны, добавь фильтр до группировки:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
WHERE country IS NOT NULL
GROUP BY country
ORDER BY country;
```