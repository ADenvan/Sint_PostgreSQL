
## `NULLIF`: обратная идея

`NULLIF` часто изучают рядом с `COALESCE`.

Если `COALESCE` заменяет `NULL` нормальным значением, то `NULLIF` делает обратное: превращает выбранное значение в `NULL`.

Синтаксис:

```sql
NULLIF(value_1, value_2)
```

Если `value_1` равно `value_2`, функция вернёт `NULL`.
Если не равно — вернёт `value_1`.

Пример:

```sql
SELECT NULLIF(score, 0) AS score_or_null
FROM results;
```

Если `score = 0`, результат будет `NULL`.
Если `score = 7`, результат будет 7.