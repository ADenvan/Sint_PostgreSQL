
## Частые ошибки новичков - CREATE TABLE

### Ошибка 1. Хранить деньги во FLOAT

Плохо:
```sql
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  price FLOAT NOT NULL
);
```

Для денег так делать не стоит. `FLOAT` хранит приблизительные значения, а деньги требуют точности.

Лучше:
```sql
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  price NUMERIC(12, 2) NOT NULL
);
```

### Ошибка 2. Не ставить NOT NULL на обязательные поля

Плохо:
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT,
  display_name TEXT
);
```

Так база разрешит пользователя без email и имени.

Лучше:
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL,
  display_name TEXT NOT NULL
);
```

Если поле обязательно для нормальной работы приложения, это должно быть видно в схеме.

### Ошибка 3. Забыть UNIQUE для email или номера заказа

Плохо:
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL
);
```

Так можно создать двух пользователей с одним email.

Лучше:
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL UNIQUE
);
```

То же самое с номерами заказов, slug страниц, внешними идентификаторами платежей и другими значениями, которые не должны повторяться.

### Ошибка 4. Хранить связь без FOREIGN KEY

Плохо:
```sql
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  body TEXT NOT NULL
);
```

На вид всё нормально: есть `user_id`, значит комментарий связан с пользователем.

Но база этого не знает. Она спокойно примет комментарий с `user_id`, которого нет в таблице пользователей.

Лучше:
```sql
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(id),
  body TEXT NOT NULL
);
```

Теперь связь — не просто договорённость в голове разработчика, а настоящее правило базы данных.

### Ошибка 5. Думать, что FOREIGN KEY сам создаст индекс

Плохо думать так:
```sql
user_id INT NOT NULL REFERENCES users(id)
```
и считать, что индекс появился автоматически.

В PostgreSQL индекс на дочернюю колонку нужно добавить отдельно:
```sql
CREATE INDEX comments_user_id_idx ON comments(user_id);
```

`FOREIGN KEY` защищает данные, но не всегда ускоряет ваши запросы.

### Ошибка 6. Использовать неудобные имена

Плохо:
```sql
CREATE TABLE "Order Items" (
  "Order ID" INT
);
```

Лучше:
```sql
CREATE TABLE order_items (
  order_id INT
);
```
Чем проще имена, тем приятнее потом писать `SELECT`, `JOIN`, `UPDATE` и любые другие запросы.

### Ошибка 7. Забыть DEFAULT для created_at

Плохо:
```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  created_at TIMESTAMPTZ NOT NULL
);
```
Теперь при каждом `INSERT` нужно помнить про `created_at`.

Лучше:
```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

Теперь база сама подставит дату создания.

### Ошибка 8. Делать слишком много nullable-колонок

Плохо:
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT,
  company_name TEXT,
  company_tax_id TEXT,
  student_group TEXT,
  teacher_subject TEXT
);
```

Если в одной таблице смешиваются обычные пользователи, компании, студенты и преподаватели, половина колонок будет постоянно `NULL`.

Это сигнал, что модель данных, возможно, стоит разделить на несколько таблиц.

Например:
- `users`;
- `company_profiles`;
- `student_profiles`;
- `teacher_profiles`.

Не всегда нужно дробить сразу, но если таблица превращается в поле из `NULL`, стоит остановиться и подумать.