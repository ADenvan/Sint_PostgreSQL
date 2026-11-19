
### Использовать алиас в HAVING и ждать, что везде сработает

Ненадёжный вариант:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING users_count > 100;
```

Более переносимый вариант:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING COUNT(*) > 100;
```

В `HAVING` лучше повторять агрегатное выражение явно.