
## `CASE` в `WHERE`

`CASE` можно использовать и в `WHERE`, но с ним нужно быть аккуратнее.

Иногда новички пишут слишком сложно:

```sql
SELECT
  id,
  amount
FROM orders
WHERE
  CASE
    WHEN amount > 1000 THEN TRUE
    ELSE FALSE
  END;
```

Такой запрос можно заменить обычным условием:

```sql
SELECT
  id,
  amount
FROM orders
WHERE amount > 1000;
```

`CASE` в `WHERE` нужен только тогда, когда условие действительно ветвится.

Например, логика зависит от роли пользователя:

```sql
SELECT
  id,
  customer_id,
  amount
FROM orders
WHERE
  CASE
    WHEN :role = 'admin' THEN TRUE
    WHEN :role = 'user' THEN customer_id = :user_id
    ELSE FALSE
  END;
```

Идея такая:

- админ видит все заказы;
- обычный пользователь видит только свои;
- неизвестная роль не видит ничего.

Такой запрос уже действительно использует ветвление.

Но в реальных проектах подобную логику часто стараются писать проще через обычные `AND` и `OR`, чтобы оптимизатору базы было легче работать с условиями.