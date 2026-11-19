
## HAVING и алиасы из SELECT

Частый вопрос: можно ли в `HAVING` использовать алиас из `SELECT`?

Например, хочется написать так:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING users_count > 100;
```

В некоторых базах данных такой запрос может сработать, например в MySQL. Но в PostgreSQL такой вариант обычно не работает: `HAVING` не видит алиас `users_count` из `SELECT`.

Более надёжный и переносимый вариант — повторить выражение:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING COUNT(*) > 100;
```

Да, выражение повторяется. Но зато запрос понятный и лучше переносится между разными СУБД.

В `ORDER BY` алиас использовать обычно можно:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING COUNT(*) > 100
ORDER BY users_count DESC;
```

Здесь `ORDER BY users_count DESC` уже работает с итоговым результатом, где алиас известен.