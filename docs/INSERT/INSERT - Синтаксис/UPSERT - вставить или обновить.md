
## UPSERT: вставить или обновить

Очень частая задача: «добавь строку, но если такая уже есть — обнови её».

Например, пользователь уже существует по email. Мы не хотим создавать дубль. Мы хотим обновить его имя или дату последнего входа.
В PostgreSQL это делается через `ON CONFLICT`.
^i2
```sql
INSERT INTO users (email, display_name, last_login_at)
VALUES ('anya@example.com', 'Anya', NOW())
ON CONFLICT (email) DO UPDATE
SET
  last_login_at = EXCLUDED.last_login_at,
  display_name = EXCLUDED.display_name;
```

^9d2c26

Такой запрос называется upsert: смесь `INSERT` и `UPDATE`.

Логика такая:
1. База пытается вставить новую строку.
2. Если строки с таким `email` ещё нет, вставка проходит успешно.
3. Если строка с таким `email` уже есть, возникает конфликт.
4. Вместо ошибки выполняется `UPDATE`.

Здесь важна псевдо-таблица `EXCLUDED`.
`EXCLUDED` хранит значения, которые мы пытались вставить.

В запросе:
```sql
VALUES ('anya@example.com', 'Anya', NOW())
```
мы пытались вставить новое имя и новое время входа. Если произошёл конфликт, эти значения можно взять через `EXCLUDED.display_name` и `EXCLUDED.last_login_at`.

То есть строка:

```sql
display_name = EXCLUDED.display_name
```
означает: «обнови имя на то значение, которое пришло в новой вставке».