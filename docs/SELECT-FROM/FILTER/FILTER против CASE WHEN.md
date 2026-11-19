
## FILTER против CASE WHEN

До появления `FILTER` условные агрегаты часто писали через `CASE WHEN`.

Например, количество оплаченных заказов:

```sql
SELECT
  COUNT(CASE WHEN status = 'paid' THEN 1 END) AS paid_orders
FROM orders;
```

Или выручка по оплаченным заказам:

```sql
SELECT
  SUM(CASE WHEN status = 'paid' THEN amount END) AS revenue_paid
FROM orders;
```

Это рабочий вариант.

Но с `FILTER` тот же смысл читается проще:

```sql
SELECT
  COUNT(*) FILTER (WHERE status = 'paid') AS paid_orders,
  SUM(amount) FILTER (WHERE status = 'paid') AS revenue_paid
FROM orders;
```

В варианте с `FILTER` сразу видно:

```text
что считаем: COUNT(*) или SUM(amount)
по каким строкам: WHERE status = 'paid'
```

А в варианте с `CASE WHEN` нужно внимательнее читать выражение внутри агрегата.

Можно сказать так:

> `CASE WHEN` прячет условие внутри выражения. `FILTER` показывает условие рядом с агрегатом.

Для отчётов это обычно приятнее и понятнее.