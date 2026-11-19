
## Скалярный подзапрос в UPDATE

Скалярный подзапрос можно использовать и при обновлении данных.

Например, в таблице `customers` есть колонка `total_spent`, куда нужно записать сумму заказов каждого клиента.

```sql
UPDATE customers c
SET total_spent = COALESCE((
  SELECT SUM(o.amount)
  FROM orders o
  WHERE o.customer_id = c.id
), 0);
```

Для каждой строки из `customers` база выполнит подзапрос, найдёт заказы этого клиента, посчитает сумму и запишет результат в `total_spent`.

Если заказов нет, `SUM` вернёт `NULL`, а `COALESCE` заменит его на `0`.