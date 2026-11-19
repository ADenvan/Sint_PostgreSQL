
### Использовать INNER JOIN, когда нужен LEFT JOIN

Если задача звучит так:

> Покажи всех пользователей и их заказы, если они есть.

`INNER JOIN` не подойдёт, потому что он уберёт пользователей без заказов.

Нужен `LEFT JOIN`.

```sql
SELECT
  u.name,
  o.amount
FROM users u
LEFT JOIN orders o
  ON u.id = o.user_id;
```