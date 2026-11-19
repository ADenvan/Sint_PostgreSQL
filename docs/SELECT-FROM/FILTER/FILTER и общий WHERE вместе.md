
## FILTER и общий WHERE вместе

`WHERE` и `FILTER` можно использовать вместе.

Например, мы хотим построить отчёт только за июнь 2026 года, но внутри этого периода посчитать разные статусы.

```sql
SELECT
  COUNT(*) AS orders_total,
  COUNT(*) FILTER (WHERE status = 'paid') AS paid_orders,
  COUNT(*) FILTER (WHERE status = 'refunded') AS refunded_orders,
  SUM(amount) FILTER (WHERE status = 'paid') AS revenue_paid
FROM orders
WHERE created_at >= DATE '2026-06-01'
  AND created_at <  DATE '2026-07-01';
```

Здесь общий `WHERE` ограничивает данные июнем.

А `FILTER` внутри агрегатов делит июньские заказы на сегменты.

Это очень частый паттерн для отчётов:

```text
сначала выбираем общий период
потом внутри него считаем разные метрики
```

Так меньше риска, что соседние метрики будут посчитаны по разным наборам данных.