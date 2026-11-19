
### Использовать HAVING вместо WHERE

Плохой вариант:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING country = 'RU';
```

Лучше:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
WHERE country = 'RU'
GROUP BY country;
```

Если условие можно применить к обычным строкам до группировки, используй `WHERE`.