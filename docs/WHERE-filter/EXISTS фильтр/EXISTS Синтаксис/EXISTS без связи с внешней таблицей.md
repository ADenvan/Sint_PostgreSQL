
## EXISTS без связи с внешней таблицей

Одна из частых ошибок — написать `EXISTS`, но забыть связь с внешней таблицей.

Например:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
);
```

Что делает этот запрос?

Он проверяет:

> Есть ли в таблице `orders` хотя бы одна строка вообще?

Если в `orders` есть хотя бы один заказ, условие `EXISTS` будет `TRUE` для каждого клиента. В результате вернутся все клиенты.

Если таблица `orders` пустая, не вернётся никто.

Скорее всего, это не то, что вы хотели.

Обычно внутри `EXISTS` нужна связь с внешней строкой:

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
);
```

Сравните:

```sql
WHERE EXISTS (
  SELECT 1
  FROM orders o
)
```

Это проверка существования заказов вообще.

```sql
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.id
)
```

Это проверка существования заказов у конкретного клиента.

Разница огромная.