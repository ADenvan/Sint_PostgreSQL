
## BETWEEN: значение находится в диапазоне

`BETWEEN` проверяет, попадает ли значение в диапазон.

Например, товары от `100` до `500`:

```sql
SELECT name, price
FROM products
WHERE price BETWEEN 100 AND 500;
```

Важно: `BETWEEN` включает обе границы.

То есть это условие:

```sql
WHERE price BETWEEN 100 AND 500
```

равносильно этому:

```sql
WHERE price >= 100 AND price <= 500
```

Если цена ровно `100`, строка попадёт в результат.  
Если цена ровно `500`, тоже попадёт.

`BETWEEN` часто используют с числами и датами.

```sql
SELECT id, amount, created_at
FROM orders
WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';
```

Этот запрос выбирает заказы за период от `2024-01-01` до `2024-12-31` включительно.