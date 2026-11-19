
## LIMIT не сортирует данные сам

Это важный момент.

`LIMIT 10` не значит:

- первые 10 по `id`;
- последние 10 по дате;
- самые новые 10;
- самые популярные 10.

Он значит только одно: **вернуть не больше 10 строк**.

Порядок задаёт только `ORDER BY`.

Например, последние 10 заказов:

```sql
SELECT id, customer_id, created_at, amount
FROM orders
ORDER BY created_at DESC
LIMIT 10;
```

Самые дорогие 10 заказов:

```sql
SELECT id, customer_id, created_at, amount
FROM orders
ORDER BY amount DESC
LIMIT 10;
```

Первые 10 пользователей по `id`:

```sql
SELECT id, email, created_at
FROM users
ORDER BY id ASC
LIMIT 10;
```

Три разных вопроса — три разных сортировки.