
## Что будет, если под FILTER не попала ни одна строка

У агрегатов разное поведение, когда подходящих строк нет.

`COUNT` возвращает `0`.

Например:

```sql
SELECT
  COUNT(*) FILTER (WHERE status = 'unknown') AS unknown_orders
FROM orders;
```

Если таких заказов нет, результат будет:

```text
unknown_orders
--------------
0
```

А вот `SUM`, `AVG`, `MIN`, `MAX` обычно вернут `NULL`.

Например:

```sql
SELECT
  SUM(amount) FILTER (WHERE status = 'unknown') AS unknown_amount
FROM orders;
```

Если подходящих строк нет, результат будет:

```text
unknown_amount
--------------
NULL
```

Для отчётов это часто неудобно. На дашборде обычно хочется видеть `0`, а не `NULL`.

В таком случае используют `COALESCE`.
^f2
```sql
SELECT
  COALESCE(
    SUM(amount) FILTER (WHERE status = 'unknown'),
    0
  ) AS unknown_amount
FROM orders;
```

^b8be08

Теперь, если строк нет, результат будет `0`.

Можно запомнить так:

> `COUNT` при отсутствии строк возвращает `0`. `SUM` и `AVG` могут вернуть `NULL`, поэтому для отчётов часто нужен `COALESCE`.

## Пример: зарплатный отчёт по отделам

Допустим, есть таблица `employees`:

```text
id | name  | dept | salary
---+-------+------+--------
1  | Anna  | eng  | 180000
2  | Bob   | eng  | 120000
3  | Kate  | hr   | 90000
4  | Tom   | hr   | 160000
```

Хотим по каждому отделу посчитать:

- всех сотрудников;
- сотрудников с зарплатой выше 150000;
- фонд оплаты таких сотрудников.

```sql
SELECT
  dept,
  COUNT(*) AS employees_total,
  COUNT(*) FILTER (WHERE salary > 150000) AS high_salary_employees,
  COALESCE(
    SUM(salary) FILTER (WHERE salary > 150000),
    0
  ) AS high_salary_payroll
FROM employees
GROUP BY dept
ORDER BY dept;
```

Результат:

```text
dept | employees_total | high_salary_employees | high_salary_payroll
-----+-----------------+-----------------------+--------------------
eng  | 2               | 1                     | 180000
hr   | 2               | 1                     | 160000
```

Если в каком-то отделе не будет сотрудников с зарплатой выше 150000, `COUNT` вернёт `0`, а `SUM` без `COALESCE` вернул бы `NULL`.