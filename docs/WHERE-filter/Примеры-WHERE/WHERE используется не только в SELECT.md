
## WHERE используется не только в SELECT

Чаще всего `WHERE` изучают вместе с `SELECT`, но он нужен не только для чтения.

`WHERE` также используется в `UPDATE` и `DELETE`.

Например, изменить тариф только одному пользователю:

```sql
UPDATE users
SET tier = 'gold'
WHERE id = 1;
```

Удалить только отменённые заказы:

```sql
DELETE FROM orders
WHERE status = 'cancelled';
```

Вот почему важно хорошо понимать `WHERE`.

В `SELECT` ошибка просто покажет не те строки.  
В `UPDATE` ошибка может изменить не те строки.  
В `DELETE` ошибка может удалить не те строки.

Особенно опасны запросы без `WHERE`.

```sql
UPDATE users
SET tier = 'gold';
```

Такой запрос обновит всех пользователей.

```sql
DELETE FROM orders;
```

Такой запрос удалит все строки из `orders`.

Поэтому перед важными `UPDATE` и `DELETE` полезно сначала сделать проверочный `SELECT` с тем же условием.

```sql
SELECT id, email, tier
FROM users
WHERE id = 1;
```

Сначала посмотрели, потом изменили.