
## ON DELETE SET NULL

Есть ещё вариант: при удалении родителя оставить дочерние строки, но убрать ссылку.

```sql
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE SET NULL,
  body TEXT NOT NULL
);
```
Если удалить пользователя, комментарии останутся, но `user_id` станет `NULL`.

Это подходит, когда дочерняя запись может жить без родителя.
Например, можно оставить комментарий, но показывать автора как удалённого пользователя.

Важно: колонка должна разрешать `NULL`. Если написать так:
```sql
user_id INT NOT NULL REFERENCES users(id) ON DELETE SET NULL
```
возникнет конфликт: действие хочет поставить `NULL`, а колонка запрещает `NULL`.