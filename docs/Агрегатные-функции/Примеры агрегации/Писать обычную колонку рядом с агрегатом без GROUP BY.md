
## Писать обычную колонку рядом с агрегатом без `GROUP BY`

Неправильно:

```sql
SELECT
  name,
  COUNT(*) AS users_count
FROM users;
```

Правильно:

```sql
SELECT
  name,
  COUNT(*) AS users_count
FROM users
GROUP BY name;
```

Если хочешь получить количество пользователей по каждому имени, нужен `GROUP BY name`.

Если хочешь получить только общее количество, убери `name`:

```sql
SELECT COUNT(*) AS users_count
FROM users;
```