
### Добавить в SELECT колонку, которой нет в GROUP BY

Плохой вариант:

```sql
SELECT
  country,
  name,
  COUNT(*) AS users_count
FROM users
GROUP BY country;
```

Проблема: в одной стране может быть много имён. База не знает, какое имя показать.

Правильный вариант:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country;
```

Или, если нужна группировка ещё и по имени:

```sql
SELECT
  country,
  name,
  COUNT(*) AS users_count
FROM users
GROUP BY country, name;
```