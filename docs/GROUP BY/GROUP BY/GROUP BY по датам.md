
## GROUP BY по датам

С датами нужно быть аккуратным.

Если сгруппировать по полной дате и времени, можно получить слишком много групп.

Например:

```sql
SELECT
  created_at,
  COUNT(*) AS orders_count
FROM orders
GROUP BY created_at;
```

Если `created_at` содержит точное время до секунд, почти каждый заказ может оказаться в отдельной группе.

Для отчётов чаще группируют не по полной дате, а по периоду: день, месяц, год.

Например, заказы по дням:

```sql
SELECT
  DATE_TRUNC('day', created_at) AS day,
  COUNT(*) AS orders_count
FROM orders
GROUP BY 1
ORDER BY 1;
```

Заказы по месяцам:

```sql
SELECT
  DATE_TRUNC('month', created_at) AS month,
  COUNT(*) AS orders_count
FROM orders
GROUP BY 1
ORDER BY 1;
```

`DATE_TRUNC('month', created_at)` обрезает дату до начала месяца.

Например:

|created_at|month|
|---|---|
|2026-03-15 10:30:00|2026-03-01 00:00:00|
|2026-03-22 18:10:00|2026-03-01 00:00:00|
|2026-04-02 09:00:00|2026-04-01 00:00:00|

Так мартовские даты попадут в одну группу, апрельские — в другую.