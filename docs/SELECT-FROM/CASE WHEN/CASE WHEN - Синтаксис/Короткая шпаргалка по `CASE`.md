
## Короткая шпаргалка по `CASE`

Категория по диапазону:

```sql
SELECT
  amount,
  CASE
    WHEN amount >= 5000 THEN 'large'
    WHEN amount >= 1000 THEN 'medium'
    ELSE 'small'
  END AS amount_group
FROM orders;
```

Подпись по статусу:

```sql
SELECT
  status,
  CASE status
    WHEN 'pending' THEN 'waiting'
    WHEN 'paid' THEN 'paid'
    WHEN 'cancelled' THEN 'cancelled'
    ELSE 'unknown'
  END AS status_label
FROM orders;
```

Условный подсчёт:

```sql
SELECT
  country,
  SUM(CASE WHEN tier = 'free' THEN 1 ELSE 0 END) AS free_users,
  SUM(CASE WHEN tier = 'gold' THEN 1 ELSE 0 END) AS gold_users
FROM users
GROUP BY country;
```

Условная сортировка:

```sql
SELECT
  id,
  status,
  created_at
FROM orders
ORDER BY
  CASE status
    WHEN 'paid' THEN 1
    WHEN 'pending' THEN 2
    ELSE 3
  END,
  created_at DESC;
```

Проверка на `NULL`:

```sql
SELECT
  id,
  CASE
    WHEN phone IS NULL THEN 'no_phone'
    ELSE 'has_phone'
  END AS phone_status
FROM users;
```