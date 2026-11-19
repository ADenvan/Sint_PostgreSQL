
## DELETE vs UPDATE

Иногда новичок путает `DELETE` и `UPDATE`.
Если нужно изменить значение в строке, нужен `UPDATE`.

Например, пользователь поменял email:
```sql
UPDATE users
SET email = 'new_bob@example.com'
WHERE id = 2;
```
Строка осталась, изменился только email.

Если нужно убрать пользователя целиком, нужен `DELETE`:
```sql
DELETE FROM users
WHERE id = 2;
```
Строка исчезла.

Простой ориентир:
- поменять данные внутри строки — `UPDATE`;
- убрать строку из таблицы — `DELETE`.