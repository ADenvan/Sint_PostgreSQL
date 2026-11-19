
## LIMIT 1: найти одну строку

Очень частый случай — получить одну строку.

Например, самый дорогой товар:

```sql
SELECT id, name, price
FROM products
ORDER BY price DESC
LIMIT 1;
```

Последний зарегистрированный пользователь:

```sql
SELECT id, email, created_at
FROM users
ORDER BY created_at DESC, id DESC
LIMIT 1;
```

Первый заказ клиента:

```sql
SELECT id, customer_id, created_at, amount
FROM orders
WHERE customer_id = 7
ORDER BY created_at ASC, id ASC
LIMIT 1;
```

`LIMIT 1` хорош, когда тебе действительно нужна одна строка: самая новая, самая старая, самая дорогая, первая по рейтингу.

Но снова важна сортировка. Без `ORDER BY` запрос «дай одну строку» не означает «дай правильную одну строку».