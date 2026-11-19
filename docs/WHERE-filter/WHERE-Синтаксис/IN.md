
## IN: значение входит в список

`IN` используют, когда нужно проверить значение по списку вариантов.

Например, нужны пользователи из нескольких стран:

```sql
SELECT id, name, country
FROM users
WHERE country IN ('Russia', 'Belarus', 'Kazakhstan');
```

Это короче и понятнее, чем длинная цепочка через `OR`:

```sql
SELECT id, name, country
FROM users
WHERE country = 'Russia'
   OR country = 'Belarus'
   OR country = 'Kazakhstan';
```

Смысл один и тот же, но `IN` читается спокойнее.

`IN` хорошо подходит для статусов, категорий, стран, идентификаторов и любых случаев, где есть набор допустимых значений.

Например:

```sql
SELECT id, status, amount
FROM orders
WHERE status IN ('paid', 'shipped', 'delivered');
```