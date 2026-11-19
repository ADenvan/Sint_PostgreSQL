
## Группировка по `CASE`

Иногда нужно сгруппировать строки не по готовой колонке, а по категории, которую мы вычисляем сами.
Например, хотим объединить пользователей в две группы:
- `paid` — если тариф `gold` или `platinum`;
- `free` — все остальные.

```sql
SELECT
  CASE
    WHEN tier IN ('gold', 'platinum') THEN 'paid'
    ELSE 'free'
  END AS plan_group,
  COUNT(*) AS users_count
FROM users
GROUP BY
  CASE
    WHEN tier IN ('gold', 'platinum') THEN 'paid'
    ELSE 'free'
  END;
```

Результат может быть таким:

|plan_group|users_count|
|---|--:|
|free|1200|
|paid|340|

Да, выражение `CASE` пришлось повторить в `GROUP BY`.
Это обычная ситуация: база должна понимать, по какому именно выражению группировать строки.
Если повтор кажется слишком громоздким, можно вынести расчёт в CTE:

```sql
WITH users_with_plan_group AS (
  SELECT
    id,
    CASE
      WHEN tier IN ('gold', 'platinum') THEN 'paid'
      ELSE 'free'
    END AS plan_group
  FROM users
)
SELECT
  plan_group,
  COUNT(*) AS users_count
FROM users_with_plan_group
GROUP BY plan_group;
```

Так запрос читается спокойнее: сначала мы подготовили категорию, потом сгруппировали по ней.