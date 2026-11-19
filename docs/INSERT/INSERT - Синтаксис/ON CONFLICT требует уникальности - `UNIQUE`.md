
## ON CONFLICT требует уникальности - `UNIQUE`

`ON CONFLICT (email)` работает только если база понимает, что по `email` вообще может быть конфликт.
Для этого на колонке должно быть уникальное ограничение:
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  display_name TEXT NOT NULL,
  country TEXT
);
```

Или отдельный уникальный индекс:
```sql
CREATE UNIQUE INDEX users_email_key
ON users (email);
```
Без `UNIQUE`, `PRIMARY KEY` или подходящего ограничения PostgreSQL не знает, что считать конфликтом. Для базы две строки с одинаковым email — это просто две строки, если ты заранее не сказал ей: «email должен быть уникальным».