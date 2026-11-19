
## IN и EXISTS: в чём разница

Для проверки «есть ли связанные строки» часто можно написать запрос двумя способами.

Через `IN`:

```sql
SELECT *
FROM customers
WHERE id IN (
  SELECT customer_id
  FROM orders
);
```

Через `EXISTS`:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

Оба запроса отвечают на один вопрос:

> Покажи клиентов, у которых есть хотя бы один заказ.

Но стиль разный.

`IN` говорит:

> Возьми список `customer_id` из заказов и проверь, входит ли `customers.id` в этот список.

`EXISTS` говорит:

> Для каждого клиента проверь, существует ли хотя бы один заказ этого клиента.

## Когда удобнее IN

`IN` хорошо читается, когда подзапрос возвращает один простой список значений.

Например:

```sql
SELECT *
FROM orders
WHERE customer_id IN (
  SELECT id
  FROM customers
  WHERE tier = 'gold'
);
```

Или:

```sql
SELECT *
FROM products
WHERE category_id IN (
  SELECT id
  FROM categories
  WHERE is_active = true
);
```

Это выглядит естественно:

> Значение должно быть в списке.

Если задача именно такая, `IN` — хороший выбор.

## Когда удобнее EXISTS

`EXISTS` удобнее, когда условие связано с несколькими колонками или когда нужна проверка существования строки.

Например, нужно найти пользователей, у которых есть оплаченный заказ дороже 1000.

```sql
SELECT *
FROM users u
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.id
    AND o.status = 'paid'
    AND o.amount > 1000
);
```

Можно написать похожее через `IN`, но `EXISTS` здесь читается яснее:

> Покажи пользователя, если существует подходящий заказ.

Особенно хорошо `EXISTS` подходит для `NOT EXISTS`:

```sql
SELECT *
FROM users u
WHERE NOT EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.id
);
```

Это понятный способ найти пользователей без заказов.