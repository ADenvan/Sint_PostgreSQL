
## `COUNT(*)`, `COUNT(column)` и `COUNT(DISTINCT column)`

У `COUNT` есть несколько важных форм.

### `COUNT(*)` считает все строки

```sql
SELECT COUNT(*) AS all_rows
FROM users;
```

`COUNT(*)` не смотрит, заполнены ли отдельные колонки. Ему важно только количество строк.

Если строка есть — она считается.

### `COUNT(column)` считает только заполненные значения

```sql
SELECT COUNT(email) AS users_with_email
FROM users;
```

Такой запрос посчитает только строки, где `email` не равен `NULL`.

В нашей таблице:

|id|name|email|
|--:|---|---|
|1|Anna|[anna@example.com](mailto:anna@example.com)|
|2|Bob|NULL|
|3|Vera|[vera@example.com](mailto:vera@example.com)|
|4|Bob|[bob@example.com](mailto:bob@example.com)|

Результат будет:

|users_with_email|
|--:|
|3|

Пользователей четыре, но email указан только у трёх.

Это важная разница:

```sql
SELECT
  COUNT(*) AS all_rows,
  COUNT(email) AS users_with_email
FROM users;
```

Результат:

|all_rows|users_with_email|
|--:|--:|
|4|3|

`COUNT(*)` отвечает на вопрос «сколько строк?».

`COUNT(email)` отвечает на вопрос «в скольких строках заполнен email?».

### `COUNT(DISTINCT column)` считает уникальные значения

Если нужно посчитать не все значения, а только разные, используют `DISTINCT`.

```sql
SELECT COUNT(DISTINCT name) AS unique_names
FROM users;
```

В таблице два пользователя с именем Bob, но имя считается один раз.

Результат:

|unique_names|
|--:|
|3|

Потому что уникальные имена такие: Anna, Bob, Vera.

Чаще всего `COUNT(DISTINCT ...)` используют, когда нужно посчитать уникальных пользователей, клиентов, товаров или сессии:

```sql
SELECT COUNT(DISTINCT customer_id) AS unique_customers
FROM orders;
```