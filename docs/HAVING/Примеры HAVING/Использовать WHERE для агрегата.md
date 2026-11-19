
### Использовать WHERE для агрегата

Плохой вариант:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
WHERE COUNT(*) > 100
GROUP BY country;
```

Так нельзя: `WHERE` не знает результата `COUNT(*)`.

Правильно:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING COUNT(*) > 100;
```