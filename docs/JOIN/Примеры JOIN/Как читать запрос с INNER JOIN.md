
## Как читать запрос с INNER JOIN

Возьмём запрос:

```sql
SELECT
  u.name,
  p.name AS product,
  o.amount
FROM users u
JOIN orders o
  ON o.user_id = u.id
JOIN products p
  ON p.id = o.product_id
WHERE o.amount > 1000
ORDER BY o.amount DESC;
```

Читать его удобно так:

1. Берём пользователей из `users`.
2. Соединяем их с заказами из `orders`.
3. Соединяем заказы с товарами из `products`.
4. Оставляем только заказы дороже 1000.
5. Сортируем от самых дорогих к более дешёвым.
6. Показываем имя пользователя, товар и сумму заказа.

Такой способ чтения помогает не теряться, когда запрос становится длиннее.