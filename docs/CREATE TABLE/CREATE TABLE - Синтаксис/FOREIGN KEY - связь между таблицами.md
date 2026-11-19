
## FOREIGN KEY: связь между таблицами

`FOREIGN KEY` нужен, чтобы связать одну таблицу с другой.

Например, есть таблица пользователей:
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL
);
```

И есть таблица комментариев:

```sql
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(id),
  body TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```
Колонка `user_id` ссылается на `users(id)`.

Это значит: комментарий не может принадлежать пользователю, которого нет.

Если попробовать вставить комментарий с несуществующим `user_id`, база не даст этого сделать:
```sql
INSERT INTO comments (user_id, body)
VALUES (999, 'Nice post');
```
Если пользователя с `id = 999` нет, будет ошибка.

Это защищает от «осиротевших» данных: комментариев без пользователя, заказов без клиента, платежей без заказа.