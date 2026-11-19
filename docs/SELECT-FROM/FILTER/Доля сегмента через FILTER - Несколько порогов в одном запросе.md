
## Доля сегмента через FILTER

`FILTER` удобно использовать для расчёта долей.

Например, нужно посчитать долю оплаченных заказов среди всех заказов.

```sql
SELECT
  COUNT(*) FILTER (WHERE status = 'paid')::numeric / COUNT(*) AS paid_ratio
FROM orders;
```

Зачем здесь `::numeric`?

Потому что если делить целое число на целое число, можно получить целочисленное деление или потерять дробную часть в некоторых ситуациях. Приведение к `numeric` явно говорит базе, что нам нужен дробный результат.

Можно округлить долю:

```sql
SELECT
  ROUND(
    COUNT(*) FILTER (WHERE status = 'paid')::numeric / COUNT(*),
    2
  ) AS paid_ratio
FROM orders;
```

Если из 10 заказов оплачены 7, результат будет:

```text
paid_ratio
----------
0.70
```

Но здесь есть потенциальная проблема: если в таблице нет строк, `COUNT(*)` будет равен `0`, и делить на ноль нельзя.

Более безопасный вариант:

```sql
SELECT
  ROUND(
    COUNT(*) FILTER (WHERE status = 'paid')::numeric / NULLIF(COUNT(*), 0),
    2
  ) AS paid_ratio
FROM orders;
```

`NULLIF(COUNT(*), 0)` превращает ноль в `NULL`, чтобы избежать ошибки деления на ноль.

## Несколько порогов в одном запросе

`FILTER` хорошо подходит, когда нужно посчитать несколько сегментов рядом.

Например, по сотрудникам:

```sql
SELECT
  dept,
  COUNT(*) AS employees_total,
  COUNT(*) FILTER (WHERE salary >= 100000) AS salary_100k_plus,
  COUNT(*) FILTER (WHERE salary >= 150000) AS salary_150k_plus,
  COUNT(*) FILTER (WHERE salary >= 200000) AS salary_200k_plus
FROM employees
GROUP BY dept
ORDER BY dept;
```

Так можно быстро построить отчёт по порогам.

Ещё пример по заказам:

```sql
SELECT
  COUNT(*) AS orders_total,
  COUNT(*) FILTER (WHERE amount < 1000) AS small_orders,
  COUNT(*) FILTER (WHERE amount >= 1000 AND amount < 5000) AS medium_orders,
  COUNT(*) FILTER (WHERE amount >= 5000) AS large_orders
FROM orders;
```

Каждая колонка — отдельный сегмент.

Запрос при этом остаётся одним и читается довольно прозрачно.