
## JOIN трёх таблиц

`JOIN` можно цеплять один за другим.

Допустим, у нас есть три таблицы:

- `users` — пользователи;
- `orders` — заказы;
- `products` — товары.

Таблица `users`:

|id|name|
|--:|---|
|1|Anna|
|2|Boris|

Таблица `products`:

|id|name|price|
|--:|---|--:|
|100|Kettle|4500|
|101|Phone|90000|
|102|Book|2000|

Таблица `orders`:

|id|user_id|product_id|amount|
|--:|--:|--:|--:|
|10|1|100|4500|
|11|1|102|2000|
|12|2|100|4500|

Нужно получить отчёт: кто что купил.

```sql
SELECT
  u.name AS buyer,
  p.name AS product,
  o.amount
FROM users u
JOIN orders o
  ON u.id = o.user_id
JOIN products p
  ON p.id = o.product_id;
```

Результат:

|buyer|product|amount|
|---|---|--:|
|Anna|Kettle|4500|
|Anna|Book|2000|
|Boris|Kettle|4500|

Что произошло:

1. `users` соединилась с `orders` по пользователю.
2. Потом результат соединился с `products` по товару.
3. На выходе получились строки, где есть и покупатель, и заказ, и товар.

Таких соединений может быть много. В реальных проектах запросы с несколькими `JOIN` — обычное дело.