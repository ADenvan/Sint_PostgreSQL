
## GROUP BY и ORDER BY

После группировки результат можно отсортировать.

Например, найти топ-5 стран по количеству пользователей:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
ORDER BY users_count DESC
LIMIT 5;
```

Здесь `ORDER BY users_count DESC` сортирует уже готовые группы: сначала страны с большим количеством пользователей, потом с меньшим.

Можно сортировать и прямо по агрегатной функции:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
ORDER BY COUNT(*) DESC;
```

Но чаще удобнее дать агрегату понятное имя через `AS`, а потом сортировать по этому имени.