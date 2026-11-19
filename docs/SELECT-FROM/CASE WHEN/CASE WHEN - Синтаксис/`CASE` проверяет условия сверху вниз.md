
## `CASE` проверяет условия сверху вниз

Очень важное правило: условия в `CASE` проверяются по порядку.

Побеждает первое условие, которое оказалось истинным.

Например:

```sql
SELECT
  score,
  CASE
    WHEN score >= 50 THEN 'ok'
    WHEN score >= 70 THEN 'good'
    WHEN score >= 90 THEN 'excellent'
    ELSE 'failed'
  END AS result
FROM exams;
```

На первый взгляд похоже на нормальный запрос, но в нём ошибка логики.

Если `score = 95`, первое условие `score >= 50` уже истинно. Значит SQL вернёт `ok` и до условий `score >= 70` и `score >= 90` уже не дойдёт.

Поэтому диапазоны обычно пишут от более строгого условия к более мягкому:

```sql
SELECT
  score,
  CASE
    WHEN score >= 90 THEN 'excellent'
    WHEN score >= 70 THEN 'good'
    WHEN score >= 50 THEN 'ok'
    ELSE 'failed'
  END AS result
FROM exams;
```

Теперь всё правильно:

- 95 → `excellent`;
- 82 → `good`;
- 61 → `ok`;
- 40 → `failed`.

## Пример: уровни клиентов по сумме покупок

Допустим, есть таблица `users`:

|id|name|total_spent|
|--:|---|--:|
|1|Anna|250|
|2|Bob|50|
|3|Vera|12000|
|4|Georgy|1500|

Хотим присвоить каждому пользователю уровень:

- от 10000 — `platinum`;
- от 1000 — `gold`;
- от 100 — `silver`;
- меньше 100 — `bronze`.

Запрос:

```sql
SELECT
  name,
  total_spent,
  CASE
    WHEN total_spent >= 10000 THEN 'platinum'
    WHEN total_spent >= 1000 THEN 'gold'
    WHEN total_spent >= 100 THEN 'silver'
    ELSE 'bronze'
  END AS tier
FROM users;
```

Результат:

|name|total_spent|tier|
|---|--:|---|
|Anna|250|silver|
|Bob|50|bronze|
|Vera|12000|platinum|
|Georgy|1500|gold|

Здесь `CASE` создаёт новую колонку `tier`. Её не было в таблице, она появляется только в результате запроса.

Это удобно: сырые данные остаются как есть, а в отчёте мы видим уже понятную классификацию.