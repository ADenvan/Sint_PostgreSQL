
### Фильтровать агрегаты через WHERE

Плохой вариант:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
WHERE COUNT(*) > 100
GROUP BY country;
```

Так нельзя, потому что `WHERE` работает до группировки.

Правильный вариант:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING COUNT(*) > 100;
```

`HAVING` работает после группировки и умеет фильтровать по агрегатам.