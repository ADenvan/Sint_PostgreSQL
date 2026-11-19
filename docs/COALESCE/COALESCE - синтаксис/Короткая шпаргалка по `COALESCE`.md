
## Короткая шпаргалка по `COALESCE`

Первое не `NULL` значение:

```sql
SELECT COALESCE(NULL, 'hello', 'world') AS result;
```

Fallback для имени пользователя:

```sql
SELECT COALESCE(nickname, full_name, 'Guest') AS display_name
FROM users;
```

Замена `NULL` на 0 в арифметике:

```sql
SELECT
  COALESCE(points, 0) + COALESCE(bonus, 0) AS total_score
FROM users;
```

Ноль вместо `NULL` для пустой суммы:

```sql
SELECT COALESCE(SUM(amount), 0) AS total_amount
FROM orders;
```

Обработка пустой строки и `NULL`:

```sql
SELECT COALESCE(NULLIF(value, ''), 'default') AS clean_value
FROM settings;
```

Защита от деления на ноль:

```sql
SELECT
  COALESCE(total_amount / NULLIF(orders_count, 0), 0) AS avg_order_amount
FROM customer_stats;
```

Проверка `NULL` в фильтре:

```sql
SELECT *
FROM users
WHERE deleted_at IS NULL;
```