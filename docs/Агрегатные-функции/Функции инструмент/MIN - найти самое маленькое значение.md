
## `MIN` — найти самое маленькое значение

`MIN` возвращает минимальное значение в колонке.

Например, самый дешёвый товар:

```sql
SELECT MIN(price) AS cheapest_price
FROM products;
```

Результат:

|cheapest_price|
|--:|
|990|

`MIN` работает не только с числами.

Можно найти самую раннюю дату заказа:

```sql
SELECT MIN(created_at) AS first_order_date
FROM orders;
```

Или первое имя по алфавитному порядку:

```sql
SELECT MIN(name) AS first_name
FROM users;
```