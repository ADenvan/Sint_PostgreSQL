
## COUNT DISTINCT с FILTER

`FILTER` можно использовать вместе с `DISTINCT`.

Например, нужно посчитать:

- всех пользователей, которые делали заказы;
- пользователей с оплаченными заказами;
- пользователей с возвратами.

```sql
SELECT
  COUNT(DISTINCT user_id) AS users_with_any_orders,
  COUNT(DISTINCT user_id) FILTER (WHERE status = 'paid') AS users_with_paid_orders,
  COUNT(DISTINCT user_id) FILTER (WHERE status = 'refunded') AS users_with_refunds
FROM orders;
```

Здесь важно, что `FILTER` пишется после агрегата:

```sql
COUNT(DISTINCT user_id) FILTER (WHERE status = 'paid')
```

Такой запрос считает уникальных пользователей только среди строк, где статус равен `paid`.

Это полезно для продуктовой аналитики: можно считать не только количество событий, но и количество уникальных пользователей в каждом сегменте.