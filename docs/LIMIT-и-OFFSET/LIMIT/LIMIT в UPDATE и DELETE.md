
## LIMIT в UPDATE и DELETE

В обычных `SELECT` с `LIMIT` всё просто. Но с `UPDATE` и `DELETE` есть отличия между базами.

В MySQL можно написать:

```sql
DELETE FROM logs
WHERE created_at < '2024-01-01'
LIMIT 100;
```

Это удалит не больше 100 строк.

В PostgreSQL такого синтаксиса для `DELETE ... LIMIT` нет. Обычно используют подзапрос или CTE.

Например, удалить 100 старых логов в PostgreSQL:

```sql
WITH rows_to_delete AS (
  SELECT id
  FROM logs
  WHERE created_at < '2024-01-01'
  ORDER BY id
  LIMIT 100
)
DELETE FROM logs
WHERE id IN (
  SELECT id
  FROM rows_to_delete
);
```

С `UPDATE` похожая история: в PostgreSQL прямого `UPDATE ... LIMIT` нет, но можно сначала выбрать нужные `id`, а потом обновить строки по ним.

```sql
WITH rows_to_update AS (
  SELECT id
  FROM tasks
  WHERE status = 'new'
  ORDER BY id
  LIMIT 100
)
UPDATE tasks
SET status = 'processing'
WHERE id IN (
  SELECT id
  FROM rows_to_update
);
```

Для начинающего главный вывод такой: `LIMIT` в `SELECT` есть почти везде, а вот `LIMIT` в `UPDATE` и `DELETE` зависит от конкретной СУБД.