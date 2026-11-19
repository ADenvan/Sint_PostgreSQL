
## FOREIGN KEY не создаёт индекс автоматически

Это частая ловушка новичков.
В PostgreSQL внешний ключ на дочерней колонке не создаёт индекс автоматически.

Например:
```sql
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(id),
  body TEXT NOT NULL
);
```
Связь есть. База проверяет, что `user_id` существует в `users`.

Но индекса на `comments(user_id)` автоматически нет.

Если комментариев много, запросы по `user_id` могут работать медленнее:
```sql
SELECT *
FROM comments
WHERE user_id = 10;
```

Поэтому индекс часто добавляют отдельно:

```sql
CREATE INDEX comments_user_id_idx ON comments(user_id);
```

Особенно это важно, если вы часто:
- ищете дочерние строки по родителю;
- удаляете родительские строки;
- делаете `JOIN` по внешнему ключу;
- проверяете связанные данные в больших таблицах.

Запомните коротко:
**`FOREIGN KEY` отвечает за правильность данных, а индекс — за скорость поиска.**
Это разные вещи.

## Полный пример: пользователи и заказы

Соберём небольшой пример ближе к реальному проекту.

Есть пользователи:
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  display_name TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

Есть заказы:

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(id),
  number TEXT NOT NULL UNIQUE,
  amount NUMERIC(12, 2) NOT NULL CHECK (amount > 0),
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'paid', 'cancelled')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

И добавим индекс на внешний ключ:

```sql
CREATE INDEX orders_user_id_idx ON orders(user_id);
```

Теперь база защищает нас от многих ошибок:

- нельзя создать заказ без пользователя;
- нельзя создать заказ на отрицательную сумму;
- нельзя записать неизвестный статус;
- нельзя повторить номер заказа;
- дата создания подставится сама;
- заказы пользователя можно быстрее находить по `user_id`.

Вот так `CREATE TABLE` превращается из простой команды в фундамент нормальной структуры данных.