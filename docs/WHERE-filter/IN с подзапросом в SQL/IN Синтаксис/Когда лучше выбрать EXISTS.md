
## Когда лучше выбрать EXISTS

Выбирай `EXISTS`, когда:

- нужно проверить существование связанной строки;
- условие зависит от нескольких колонок;
- пишешь обратную проверку через `NOT EXISTS`;
- хочешь избежать ловушек `NOT IN` с `NULL`.

Например:

```sql
SELECT *
FROM users u
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.id
    AND o.status = 'paid'
);
```

И особенно:

```sql
SELECT *
FROM users u
WHERE NOT EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.id
);
```

Для поиска строк «без пары» `NOT EXISTS` обычно самый понятный и безопасный вариант.