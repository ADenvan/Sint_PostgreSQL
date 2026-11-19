
## `NULLIF` для безопасного деления

Самый практичный пример `NULLIF` — защита от деления на ноль.

Обычный запрос:

```sql
SELECT total_amount / orders_count AS avg_order_amount
FROM customer_stats;
```

Если `orders_count = 0`, база получит деление на ноль. Это ошибка.

Можно защититься так:

```sql
SELECT total_amount / NULLIF(orders_count, 0) AS avg_order_amount
FROM customer_stats;
```

Что происходит?

Если `orders_count` равен 0, выражение:

```sql
NULLIF(orders_count, 0)
```

вернёт `NULL`.

А деление на `NULL` даст `NULL`, а не ошибку деления на ноль.
Если хочется вместо `NULL` получить 0, можно добавить `COALESCE`:

```sql
SELECT
  COALESCE(total_amount / NULLIF(orders_count, 0), 0) AS avg_order_amount
FROM customer_stats;
```

Здесь вся цепочка читается так:
1. Если `orders_count` равен 0, преврати его в `NULL`.
2. Деление на `NULL` даст `NULL`.
3. Если итог получился `NULL`, покажи 0.

Для отчётов это очень полезный приём.