
## Базовый синтаксис EXISTS

Общий шаблон выглядит так:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

Разберём идею по шагам.

Внешний запрос идёт по таблице `customers`:

```sql
SELECT *
FROM customers c
```

Для каждого клиента проверяется условие:

```sql
WHERE EXISTS (...)
```

Внутри `EXISTS` находится подзапрос:

```sql
SELECT 1
FROM orders o
WHERE o.customer_id = c.id
```

Он ищет заказы, у которых `customer_id` совпадает с `id` текущего клиента.

Если хотя бы один заказ найден, `EXISTS` возвращает `TRUE`, и клиент попадает в результат.

Если заказов нет, `EXISTS` возвращает `FALSE`, и клиент отфильтровывается.

## Почему внутри пишут SELECT 1

Внутри `EXISTS` часто пишут:

```sql
SELECT 1
```

На первый взгляд это выглядит странно. Почему `1`? Почему не `id`, не `*`, не нужные колонки?

Потому что для `EXISTS` неважно, что именно возвращает подзапрос. Ему важно только, вернул подзапрос хотя бы одну строку или нет.

Все эти варианты по смыслу подходят:

```sql
SELECT 1
FROM orders o
WHERE o.customer_id = c.id
```

```sql
SELECT o.id
FROM orders o
WHERE o.customer_id = c.id
```

```sql
SELECT *
FROM orders o
WHERE o.customer_id = c.id
```

Но в реальных SQL-запросах чаще пишут `SELECT 1`. Это короткая и понятная идиома:

> Мы не выбираем данные, мы просто проверяем существование строки.

## Пример с клиентами и заказами

Пусть есть таблица `customers`:

|id|name|
|--:|---|
|1|Anna|
|2|Bob|
|3|Vera|
|4|Gleb|

И таблица `orders`:

|id|customer_id|amount|
|--:|--:|--:|
|1|1|100|
|2|1|250|
|3|3|80|

Нужно найти клиентов, у которых есть хотя бы один заказ.

Пишем:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

Результат:

|id|name|
|--:|---|
|1|Anna|
|3|Vera|

Почему так?

У `Anna` есть заказы:

|id|customer_id|amount|
|--:|--:|--:|
|1|1|100|
|2|1|250|

Значит, для неё `EXISTS` возвращает `TRUE`.

У `Vera` тоже есть заказ:

|id|customer_id|amount|
|--:|--:|--:|
|3|3|80|

Она тоже попадает в результат.

А у `Bob` и `Gleb` заказов нет. Для них подзапрос не находит ни одной строки, поэтому `EXISTS` возвращает `FALSE`.