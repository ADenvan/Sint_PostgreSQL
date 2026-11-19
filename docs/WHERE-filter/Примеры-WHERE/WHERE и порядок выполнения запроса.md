
## WHERE и порядок выполнения запроса

Новичку полезно понимать, что `WHERE` работает до группировки и до финального вывода результата.

Например:

```sql
SELECT country, COUNT(*) AS users_count
FROM users
WHERE is_active = TRUE
GROUP BY country;
```

Здесь база сначала оставит только активных пользователей, а уже потом сгруппирует их по стране.

Но если нужно фильтровать не обычные строки, а результат агрегации, нужен не `WHERE`, а `HAVING`.

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

Запомни так:

- `WHERE` фильтрует строки **до** группировки;
- `HAVING` фильтрует группы **после** группировки.