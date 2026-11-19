
## IN и дубликаты в подзапросе

Подзапрос внутри `IN` может вернуть дубликаты. Например:

```sql
SELECT user_id
FROM orders
WHERE status = 'paid';
```

Результат может быть таким:

|user_id|
|--:|
|1|
|1|
|1|
|3|

Для `IN` это не ломает логику.

Запрос:

```sql
SELECT *
FROM users
WHERE id IN (
  SELECT user_id
  FROM orders
  WHERE status = 'paid'
);
```

всё равно выберет пользователя `1` один раз, а не три раза.

Почему?

Потому что `IN` проверяет членство в списке: есть значение в списке или нет. Ему не важно, сколько раз оно там встретилось.

Но дубликаты могут быть лишней работой для базы. Иногда запрос можно сделать аккуратнее через `DISTINCT`:

```sql
SELECT *
FROM users
WHERE id IN (
  SELECT DISTINCT user_id
  FROM orders
  WHERE status = 'paid'
);
```

А иногда ещё лучше использовать `EXISTS`. Об этом поговорим ниже.