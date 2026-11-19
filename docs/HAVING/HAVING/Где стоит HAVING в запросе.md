
## Где стоит HAVING в запросе

`HAVING` пишется после `GROUP BY`.

Правильный порядок:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
WHERE status = 'active'
GROUP BY country
HAVING COUNT(*) > 100
ORDER BY users_count DESC;
```

Логически запрос выполняется примерно так:

1. `FROM` — берём таблицу.
2. `WHERE` — фильтруем обычные строки.
3. `GROUP BY` — собираем строки в группы.
4. `HAVING` — фильтруем группы.
5. `SELECT` — выбираем, что показать.
6. `ORDER BY` — сортируем результат.

Именно поэтому `HAVING` может работать с `COUNT(*)`, `SUM(amount)`, `AVG(rating)` и другими агрегатами: к моменту `HAVING` группы уже собраны, а агрегаты уже можно посчитать.