
## Частые ошибки новичков

### Ошибка 1. Использовать NOT IN вместо NOT EXISTS

Опасный вариант:

```sql
SELECT *
FROM customers
WHERE id NOT IN (
  SELECT customer_id
  FROM orders
);
```

Если в `orders.customer_id` есть `NULL`, результат может стать пустым или неожиданным.

Безопаснее:

```sql
SELECT *
FROM customers c
WHERE NOT EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

Для поиска отсутствующих связей почти всегда лучше `NOT EXISTS`.

### Ошибка 2. Забыть связь с внешней таблицей

Плохо:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
);
```

Этот запрос не проверяет заказы конкретного клиента. Он проверяет, есть ли заказы вообще.

Правильно:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

### Ошибка 3. Думать, что SELECT внутри EXISTS важен

Новичок может переживать, что лучше написать:

```sql
SELECT o.id
```

или:

```sql
SELECT *
```

Но для `EXISTS` содержимое `SELECT` не важно. Важно только, вернул подзапрос строку или нет.

Поэтому принято писать:

```sql
SELECT 1
```

Это коротко и ясно.

### Ошибка 4. Использовать JOIN и DISTINCT там, где нужен EXISTS

Такой запрос может работать:

```sql
SELECT DISTINCT c.*
FROM customers c
JOIN orders o ON o.customer_id = c.id;
```

Но если данные из `orders` не нужны, вариант с `EXISTS` обычно понятнее:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

`JOIN` соединяет данные.  
`EXISTS` проверяет наличие.

Это разные намерения.

### Ошибка 5. Пытаться считать строки через EXISTS

`EXISTS` не говорит, сколько строк найдено.

Если нужно просто узнать, есть ли заказы, используйте `EXISTS`:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

Если нужно узнать количество заказов, нужен `COUNT`:

```sql
SELECT
  c.id,
  c.name,
  COUNT(o.id) AS orders_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY c.id, c.name;
```

Не путайте задачи:

- `EXISTS` — есть или нет;
- `COUNT` — сколько именно.

### Ошибка 6. Добавлять LIMIT 1 без необходимости

Так писать обычно не нужно:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
  LIMIT 1
);
```

Лучше проще:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

`EXISTS` и так означает «достаточно первой найденной строки».

### Ошибка 7. Не ставить индекс на колонку связи

Запрос может быть правильным, но медленным:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

Если таблица `orders` большая, полезен индекс:

```sql
CREATE INDEX orders_customer_id_idx ON orders(customer_id);
```

Без индекса базе может быть тяжело быстро проверять наличие заказов для каждого клиента.

### Ошибка 8. Не понимать, что EXISTS возвращает boolean

`EXISTS` возвращает логическое значение: `TRUE` или `FALSE`.

Поэтому его можно использовать как условие:

```sql
WHERE EXISTS (...)
```

И как вычисляемую колонку:

```sql
SELECT
  c.id,
  EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.id
  ) AS has_orders
FROM customers c;
```

Это не список заказов и не количество заказов. Это именно флаг: да или нет.