
## IS NULL: проверка на отсутствие значения

`NULL` — одна из главных ловушек для новичков.

`NULL` в SQL означает не ноль, не пустую строку и не слово `NULL`.  
Это отсутствие значения.

Например, у пользователя может быть не заполнена дата удаления:

|id|name|deleted_at|
|--:|---|---|
|1|Anna|NULL|
|2|Bob|2024-05-10|
|3|Vera|NULL|

Если нужно найти неудалённых пользователей, нельзя писать так:

```sql
SELECT id, name
FROM users
WHERE deleted_at = NULL;
```

Это неправильная проверка.

Для `NULL` используют специальный синтаксис:

```sql
SELECT id, name
FROM users
WHERE deleted_at IS NULL;
```

Результат:

|id|name|
|--:|---|
|1|Anna|
|3|Vera|

А если нужно найти строки, где значение есть:

```sql
SELECT id, name, deleted_at
FROM users
WHERE deleted_at IS NOT NULL;
```

Результат:

|  id | name | deleted_at |
| --: | ---- | ---------- |
|   2 | Bob  | 2024-05-10 |

Правило простое:

**для `NULL` нельзя использовать `=` и `<>`. Нужны `IS NULL` и `IS NOT NULL`.**