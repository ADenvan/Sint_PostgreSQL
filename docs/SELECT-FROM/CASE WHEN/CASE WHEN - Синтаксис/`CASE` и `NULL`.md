
## `CASE` и `NULL`

С `NULL` в SQL всегда нужно быть внимательным.

Ошибка новичка:

```sql
SELECT
  id,
  CASE
    WHEN phone = NULL THEN 'no_phone'
    ELSE 'has_phone'
  END AS phone_status
FROM users;
```

Так писать нельзя.

`NULL` не сравнивается через `=`. В SQL `NULL` означает «значение отсутствует» или «значение неизвестно». Проверять его нужно через `IS NULL`.

Правильно:

```sql
SELECT
  id,
  CASE
    WHEN phone IS NULL THEN 'no_phone'
    ELSE 'has_phone'
  END AS phone_status
FROM users;
```

Для обратной проверки используют `IS NOT NULL`:

```sql
SELECT
  id,
  CASE
    WHEN phone IS NOT NULL THEN 'has_phone'
    ELSE 'no_phone'
  END AS phone_status
FROM users;
```

Это один из тех моментов, которые лучше запомнить сразу: в SQL почти никогда не нужно писать `= NULL`.

## Пример: аккуратный отчёт по заказам

Допустим, есть таблица `orders`:

|id|customer_id|status|amount|
|--:|--:|---|--:|
|1|10|paid|1200|
|2|10|pending|800|
|3|15|cancelled|500|
|4|21|paid|7000|
|5|21|refunded|7000|

Хотим получить отчёт, где:

- технические статусы сгруппированы в понятные категории;
- сумма заказа превращается в размер заказа;
- статусы сортируются в нужном порядке.

```sql
SELECT
  id,
  customer_id,
  amount,
  CASE
    WHEN status IN ('paid', 'refunded') THEN 'closed'
    WHEN status = 'pending' THEN 'open'
    WHEN status = 'cancelled' THEN 'cancelled'
    ELSE 'unknown'
  END AS status_group,
  CASE
    WHEN amount >= 5000 THEN 'large'
    WHEN amount >= 1000 THEN 'medium'
    ELSE 'small'
  END AS amount_group
FROM orders
ORDER BY
  CASE
    WHEN status = 'pending' THEN 1
    WHEN status = 'paid' THEN 2
    WHEN status = 'refunded' THEN 3
    WHEN status = 'cancelled' THEN 4
    ELSE 5
  END,
  id;
```

Такой запрос уже похож на реальный отчёт.

Мы не просто выводим сырые значения из базы. Мы сразу объясняем их:

- `status_group` показывает смысл статуса;
- `amount_group` показывает размер заказа;
- `ORDER BY CASE` задаёт понятный порядок строк.