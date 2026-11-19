
## Как безопасно писать NOT IN

Есть два способа.

Первый способ — явно убрать `NULL` из подзапроса:

```sql
SELECT *
FROM users
WHERE id NOT IN (
  SELECT user_id
  FROM orders
  WHERE user_id IS NOT NULL
);
```

Теперь подзапрос не вернёт `NULL`, и `NOT IN` будет вести себя ожидаемо.

Но в реальных задачах для такой логики чаще советуют использовать `NOT EXISTS`.

```sql
SELECT *
FROM users u
WHERE NOT EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.id
);
```

Этот запрос читается так:

> Покажи пользователя, для которого не существует ни одного заказа с таким `user_id`.

Это безопаснее при `NULL` и часто лучше читается для анти-проверок.

Практическое правило:

> Для `IN` можно использовать `IN`.  
> Для обратной проверки чаще используй `NOT EXISTS`, а не `NOT IN`.