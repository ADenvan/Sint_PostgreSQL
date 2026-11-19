
## EXISTS с дополнительными условиями

Внутри `EXISTS` можно добавлять любые условия.

Например, нужны не просто клиенты с заказами, а клиенты, у которых есть хотя бы один оплаченный заказ за последний месяц:
^e1
```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
    AND o.status = 'paid'
    AND o.created_at > NOW() - INTERVAL '1 month'
);
```

^634126

Здесь подзапрос проверяет сразу несколько вещей:

- заказ принадлежит текущему клиенту;
- заказ оплачен;
- заказ создан за последний месяц.

Если у клиента есть хотя бы один такой заказ, клиент попадёт в результат.

Это очень удобно: снаружи запрос остаётся простым, а вся логика существования связанной строки находится внутри `EXISTS`.

## Ещё пример: посты с комментариями

Пусть есть таблицы:

- `posts`;
- `comments`.

Нужно найти посты, у которых есть хотя бы один комментарий.

```sql
SELECT *
FROM posts p
WHERE EXISTS (
  SELECT 1
  FROM comments c
  WHERE c.post_id = p.id
);
```

Если нужен только посты с одобренными комментариями:

```sql
SELECT *
FROM posts p
WHERE EXISTS (
  SELECT 1
  FROM comments c
  WHERE c.post_id = p.id
    AND c.status = 'approved'
);
```

Если нужны посты без комментариев:

```sql
SELECT *
FROM posts p
WHERE NOT EXISTS (
  SELECT 1
  FROM comments c
  WHERE c.post_id = p.id
);
```

Получается очень выразительно: `EXISTS` и `NOT EXISTS` буквально читаются как «существует» и «не существует».