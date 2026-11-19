
### Забыть про NULL

Если группировать по колонке, где есть `NULL`, все `NULL` попадут в одну отдельную группу.

Если такие строки не нужны, фильтруй их заранее:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
WHERE country IS NOT NULL
GROUP BY country;
```