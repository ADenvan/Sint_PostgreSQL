
## LIMIT с агрегатами

[[Агрегаты]] - это специальные функции, которые принимают на вход набор значений

`LIMIT` часто используют после `GROUP BY`, чтобы получить топ групп.

Например, топ-5 клиентов по сумме заказов:

```sql
SELECT
  customer_id,
  SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id
ORDER BY total_amount DESC
LIMIT 5;
```

Что здесь происходит:

1. Заказы группируются по клиенту.
2. Для каждого клиента считается сумма заказов.
3. Клиенты сортируются по сумме от большей к меньшей.
4. Возвращаются первые 5 клиентов.

Это один из самых популярных видов аналитических запросов.

Ещё пример: топ-10 товаров по количеству покупок.

```sql
SELECT
  product_id,
  COUNT(*) AS purchases_count
FROM order_items
GROUP BY product_id
ORDER BY purchases_count DESC
LIMIT 10;
```

`LIMIT` здесь ограничивает уже готовый рейтинг.