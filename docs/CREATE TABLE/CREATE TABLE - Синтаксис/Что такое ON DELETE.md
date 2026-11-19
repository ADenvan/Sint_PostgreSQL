## Что такое ON DELETE

Когда есть связь между таблицами, возникает вопрос: что делать с дочерними строками, если удалить родительскую?
Например, есть пользователь и его комментарии.
Можно выбрать разное поведение.

### ON DELETE CASCADE

```sql
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  body TEXT NOT NULL
);
```
`ON DELETE CASCADE` означает: если удалить пользователя, его комментарии удалятся автоматически.

Это удобно, когда дочерние данные не имеют смысла без родителя.

Например:
- позиции заказа без заказа;
- временные токены пользователя;
- черновики, принадлежащие удалённому объекту.

Но с `CASCADE` нужно быть осторожным: одно удаление может потянуть за собой много других строк.

### ON DELETE RESTRICT

```sql
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
  body TEXT NOT NULL
);
```
`ON DELETE RESTRICT` запрещает удалять пользователя, пока у него есть комментарии.

Это безопасный вариант, когда вы не хотите случайно потерять связанные данные.

### ON DELETE SET NULL

```sql
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE SET NULL,
  body TEXT NOT NULL
);
```
`ON DELETE SET NULL` означает: если удалить пользователя, комментарий останется, но `user_id` станет `NULL`.

Важно: для этого колонка `user_id` должна разрешать `NULL`. Если написать `user_id INT NOT NULL`, то `SET NULL` не сможет сработать.

Такой вариант подходит, когда сам комментарий можно оставить, но связь с пользователем уже неизвестна или не нужна.