
## Важная особенность `SUM`: `NULL` не превращается в ноль

`SUM` пропускает значения `NULL`.

Например:

|id|amount|
|--:|--:|
|1|100|
|2|NULL|
|3|300|

Запрос:

```sql
SELECT SUM(amount) AS total_amount
FROM orders;
```

Вернёт:

|total_amount|
|--:|
|400|

`NULL` не стал нулём. Он просто не участвовал в расчёте.

Но есть важный нюанс: если подходящих строк нет или все значения равны `NULL`, результатом будет `NULL`, а не `0`.

Например:

```sql
SELECT SUM(amount) AS total_amount
FROM orders
WHERE customer_id = 999;
```

Если у клиента с таким id нет заказов, результат будет:

|total_amount|
|--:|
|NULL|

Для отчётов это часто неудобно. Обычно хочется увидеть ноль. Тогда используют `COALESCE`:

```sql
SELECT COALESCE(SUM(amount), 0) AS total_amount
FROM orders
WHERE customer_id = 999;
```

`COALESCE` говорит: если результат `SUM(amount)` оказался `NULL`, покажи вместо него `0`.