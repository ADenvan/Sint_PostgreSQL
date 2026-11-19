
### Писать HAVING до GROUP BY

Плохой вариант:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
HAVING COUNT(*) > 100
GROUP BY country;
```

Правильный порядок:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING COUNT(*) > 100;
```

`HAVING` всегда пишется после `GROUP BY`.