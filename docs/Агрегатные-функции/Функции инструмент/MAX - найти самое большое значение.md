
## `MAX` — найти самое большое значение

`MAX` возвращает максимальное значение.

Например, самый дорогой товар:

```sql
SELECT MAX(price) AS most_expensive_price
FROM products;
```

Самая поздняя дата заказа:

```sql
SELECT MAX(created_at) AS last_order_date
FROM orders;
```

Последнее имя по алфавитному порядку:

```sql
SELECT MAX(name) AS last_name
FROM users;
```

`MIN` и `MAX` тоже пропускают `NULL`.

Если все значения в колонке равны `NULL`, результат будет `NULL`.