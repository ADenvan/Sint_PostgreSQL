
### Пытаются фильтровать агрегаты через WHERE

Неправильно:

```sql
SELECT country, COUNT(*) AS users_count
FROM users
GROUP BY country
WHERE COUNT(*) > 100;
```

Правильно:

```sql
SELECT country, COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING COUNT(*) > 100;
```

`WHERE` не знает результат `COUNT(*)`, потому что он появляется позже.