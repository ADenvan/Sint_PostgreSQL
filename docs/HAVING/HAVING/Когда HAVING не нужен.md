
## Когда HAVING не нужен

`HAVING` не нужен, если ты фильтруешь обычные строки.

Например, нужны только активные пользователи:

```sql
SELECT *
FROM users
WHERE status = 'active';
```

Нужны заказы дороже 100:

```sql
SELECT *
FROM orders
WHERE amount > 100;
```

Нужны пользователи из конкретной страны:

```sql
SELECT *
FROM users
WHERE country = 'RU';
```

Во всех этих случаях нет групп и агрегатов. Значит, `HAVING` здесь лишний.