
## Simple `CASE`: когда сравниваем одну колонку с разными значениями

Есть ещё одна форма `CASE`. Она называется simple `CASE`.

Она удобна, когда мы сравниваем одну колонку с конкретными значениями.

Например, есть таблица заказов со статусами:

|id|status|
|--:|---|
|1|pending|
|2|paid|
|3|shipped|
|4|cancelled|

Хотим показать более понятную подпись для каждого статуса:

```sql
SELECT
  id,
  status,
  CASE status
    WHEN 'pending' THEN 'waiting'
    WHEN 'paid' THEN 'paid'
    WHEN 'shipped' THEN 'sent'
    WHEN 'cancelled' THEN 'cancelled'
    ELSE 'unknown'
  END AS status_label
FROM orders;
```

Здесь SQL берёт значение из колонки `status` и сравнивает его с вариантами в `WHEN`.

Это короче, чем писать так:

```sql
SELECT
  id,
  status,
  CASE
    WHEN status = 'pending' THEN 'waiting'
    WHEN status = 'paid' THEN 'paid'
    WHEN status = 'shipped' THEN 'sent'
    WHEN status = 'cancelled' THEN 'cancelled'
    ELSE 'unknown'
  END AS status_label
FROM orders;
```

Обе формы нормальные.

Simple `CASE` хорошо подходит для прямого сравнения одной колонки с набором значений.

Searched `CASE` нужен, когда условия сложнее: диапазоны, несколько колонок, `AND`, `OR`, проверки на `NULL`.