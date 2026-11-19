
## GROUP BY по месяцу: частая ловушка

Иногда хочется написать так:

```sql
SELECT
  EXTRACT(MONTH FROM created_at) AS month,
  COUNT(*) AS orders_count
FROM orders
GROUP BY 1
ORDER BY 1;
```

Такой запрос сгруппирует заказы по номеру месяца: `1`, `2`, `3` и так далее.

Но есть проблема: январь 2025 года и январь 2026 года попадут в одну группу.

Если данные только за один год — всё нормально. Если данных несколько лет — отчёт станет неправильным.

Лучше добавить год:

```sql
SELECT
  EXTRACT(YEAR FROM created_at) AS year,
  EXTRACT(MONTH FROM created_at) AS month,
  COUNT(*) AS orders_count
FROM orders
GROUP BY 1, 2
ORDER BY 1, 2;
```

Или использовать `DATE_TRUNC`:

```sql
SELECT
  DATE_TRUNC('month', created_at) AS month,
  COUNT(*) AS orders_count
FROM orders
GROUP BY 1
ORDER BY 1;
```

Для отчётов по времени `DATE_TRUNC` часто удобнее и безопаснее.