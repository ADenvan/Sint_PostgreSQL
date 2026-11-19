
## Когда использовать IN с подзапросом

Используй `IN` с подзапросом, когда условие звучит так:

- значение должно входить в список из другой таблицы;
- список заранее неизвестен;
- список можно получить отдельным `SELECT`;
- внешней таблице нужны только свои колонки;
- подзапрос возвращает одну колонку.

Хорошие примеры:

```sql
SELECT *
FROM orders
WHERE customer_id IN (
  SELECT id
  FROM customers
  WHERE tier = 'gold'
);
```

```sql
SELECT *
FROM users
WHERE id IN (
  SELECT user_id
  FROM orders
  WHERE status = 'paid'
);
```

```sql
SELECT *
FROM products
WHERE category_id IN (
  SELECT id
  FROM categories
  WHERE is_active = true
);
```

Во всех этих запросах `IN` читается естественно: значение должно быть среди значений, найденных подзапросом.