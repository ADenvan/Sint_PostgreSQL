
## Частые ошибки новичков

### Ошибка 1. Использовать NOT IN с подзапросом, где может быть NULL

Плохой вариант:

```sql
SELECT *
FROM users
WHERE id NOT IN (
  SELECT user_id
  FROM orders
);
```

Если `orders.user_id` содержит `NULL`, запрос может вернуть пустой результат.

Безопаснее так:

```sql
SELECT *
FROM users
WHERE id NOT IN (
  SELECT user_id
  FROM orders
  WHERE user_id IS NOT NULL
);
```

А чаще ещё лучше так:

```sql
SELECT *
FROM users u
WHERE NOT EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.user_id = u.id
);
```

### Ошибка 2. Вернуть несколько колонок в подзапросе

Плохой вариант:

```sql
SELECT *
FROM orders
WHERE customer_id IN (
  SELECT id, name
  FROM customers
);
```

Подзапрос для обычного `IN` должен вернуть одну колонку.

Правильно:

```sql
SELECT *
FROM orders
WHERE customer_id IN (
  SELECT id
  FROM customers
);
```

Если нужно сравнивать несколько колонок, часто лучше использовать `EXISTS`.

### Ошибка 3. Путать IN и равно

Такой запрос ожидает, что подзапрос вернёт ровно одно значение:

```sql
SELECT *
FROM orders
WHERE customer_id = (
  SELECT id
  FROM customers
  WHERE tier = 'gold'
);
```

Если `gold`-клиентов несколько, будет ошибка.

Если значений может быть много, нужен `IN`:

```sql
SELECT *
FROM orders
WHERE customer_id IN (
  SELECT id
  FROM customers
  WHERE tier = 'gold'
);
```

`=` — для одного значения.

`IN` — для списка значений.

### Ошибка 4. Забыть, что IN не умножает строки

Допустим, подзапрос вернул одного и того же клиента три раза:

|user_id|
|--:|
|1|
|1|
|1|

Запрос:

```sql
SELECT *
FROM users
WHERE id IN (
  SELECT user_id
  FROM orders
);
```

не вернёт пользователя три раза. Он просто проверит, есть ли `id` в списке.

Если тебе нужно получить по строке на каждый заказ, нужен `JOIN`, а не `IN`.

### Ошибка 5. Использовать IN там, где нужен JOIN

Если тебе нужны только пользователи, у которых есть заказы, `IN` подходит:

```sql
SELECT *
FROM users
WHERE id IN (
  SELECT user_id
  FROM orders
);
```

Но если нужно вывести ещё и сумму заказа, дату заказа или статус заказа, нужен `JOIN`:

```sql
SELECT
  u.id,
  u.name,
  o.amount,
  o.status
FROM users u
JOIN orders o ON o.user_id = u.id;
```

`IN` фильтрует. `JOIN` соединяет таблицы и позволяет брать колонки из обеих.

### Ошибка 6. Писать огромный IN-список руками

Плохо:

```sql
SELECT *
FROM users
WHERE id IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
```

Для небольшого списка нормально. Но если значений тысячи, лучше подумать о временной таблице, массиве, `JOIN` или подзапросе.

### Ошибка 7. Не учитывать NULL слева

Если значение слева само `NULL`, проверка через `IN` не даст `TRUE`.

Например:

```sql
SELECT *
FROM orders
WHERE customer_id IN (
  SELECT id
  FROM customers
);
```

Если у заказа `customer_id` равен `NULL`, такая строка не пройдёт фильтр. SQL не может сказать, что неизвестный клиент точно входит в список.

Если такие строки нужны отдельно, их надо обработать явно:

```sql
SELECT *
FROM orders
WHERE customer_id IN (
  SELECT id
  FROM customers
)
   OR customer_id IS NULL;
```