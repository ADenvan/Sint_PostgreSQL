
## Базовый синтаксис

Общий вид такой:

```sql
SELECT columns
FROM table_a
WHERE column_name IN (
  SELECT another_column
  FROM table_b
  WHERE condition
);
```

Важное правило: подзапрос внутри `IN` обычно должен возвращать одну колонку.

Например, так правильно:

```sql
SELECT *
FROM orders
WHERE customer_id IN (
  SELECT id
  FROM customers
  WHERE tier = 'gold'
);
```

А так нельзя, если ты используешь обычный `IN` для одной колонки:

```sql
SELECT *
FROM orders
WHERE customer_id IN (
  SELECT id, name
  FROM customers
);
```

Почему нельзя?

Потому что слева одно значение — `customer_id`. А справа подзапрос возвращает сразу две колонки: `id` и `name`. SQL не понимает, с чем именно сравнивать `customer_id`.

## Пример с таблицами customers и orders

Допустим, есть таблица `customers`:

|id|name|tier|
|--:|---|---|
|1|Anna|gold|
|2|Bob|free|
|3|Vera|gold|
|4|Gleb|free|

И таблица `orders`:

|id|customer_id|amount|
|--:|--:|--:|
|1|1|100|
|2|2|50|
|3|1|200|
|4|3|300|

Нужно выбрать заказы только `gold`-клиентов.

Сначала посмотрим, какой список вернёт подзапрос:

```sql
SELECT id
FROM customers
WHERE tier = 'gold';
```

Результат:

|id|
|--:|
|1|
|3|

То есть `gold`-клиенты — это клиенты с `id` 1 и 3.

Теперь используем этот список во внешнем запросе:

```sql
SELECT *
FROM orders
WHERE customer_id IN (
  SELECT id
  FROM customers
  WHERE tier = 'gold'
);
```

Результат:

|id|customer_id|amount|
|--:|--:|--:|
|1|1|100|
|3|1|200|
|4|3|300|

Заказ клиента `2` не попал в результат, потому что клиент `2` имеет тариф `free`, а не `gold`.