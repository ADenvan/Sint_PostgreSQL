
## `COALESCE` с агрегатами

Агрегатные функции тоже часто возвращают `NULL`.
Например, есть таблица `orders`:

|id|customer_id|amount|
|--:|--:|--:|
|1|10|1200|
|2|10|800|
|3|15|500|

Посчитаем сумму заказов клиента 10:

```sql
SELECT SUM(amount) AS total_amount
FROM orders
WHERE customer_id = 10;
```

Результат:

|total_amount|
|--:|
|2000|

А теперь посчитаем сумму заказов клиента, у которого заказов нет:

```sql
SELECT SUM(amount) AS total_amount
FROM orders
WHERE customer_id = 999;
```

Результат:

|total_amount|
|--:|
|NULL|

Это может удивлять новичков.

Кажется, что сумма пустого набора должна быть 0. Но SQL возвращает `NULL`: считать было нечего, результата нет.

В отчётах и интерфейсах чаще нужен 0. Тогда пишут так:

```sql
SELECT COALESCE(SUM(amount), 0) AS total_amount
FROM orders
WHERE customer_id = 999;
```

Результат:

|total_amount|
|--:|
|0|

Такой приём стоит запомнить. Он часто встречается в финансовых отчётах, личных кабинетах, админках и аналитических дашбордах.