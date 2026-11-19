
## Базовый синтаксис UPDATE

Общий вид такой:
```sql
UPDATE table_name
SET column_name = new_value
WHERE condition;
```

По частям:
- `UPDATE table_name` — какую таблицу обновляем;
- `SET column_name = new_value` — какую колонку и на какое значение меняем;
- `WHERE condition` — какие строки нужно обновить.

Например:
```sql
UPDATE users
SET tier = 'gold'
WHERE id = 1;
```

Читается так:

> В таблице `users` найди пользователя с `id = 1` и измени у него колонку `tier` на значение `'gold'`.

Вот и вся базовая идея.

## Пример с таблицей пользователей

Допустим, есть таблица `users`.

|id|name|email|tier|
|--:|---|---|---|
|1|Аня|[anya@example.com](mailto:anya@example.com)|free|
|2|Боб|[bob@example.com](mailto:bob@example.com)|free|
|3|Вера|[vera@example.com](mailto:vera@example.com)|gold|

Аня купила платный тариф. Нужно поменять её тариф с `free` на `gold`.
```sql
UPDATE users
SET tier = 'gold'
WHERE id = 1;
```

После запроса таблица станет такой:

|id|name|email|tier|
|--:|---|---|---|
|1|Аня|[anya@example.com](mailto:anya@example.com)|gold|
|2|Боб|[bob@example.com](mailto:bob@example.com)|free|
|3|Вера|[vera@example.com](mailto:vera@example.com)|gold|

Что важно заметить:
- изменилась только одна строка;
- изменилась только одна колонка;
- остальные данные Ани остались прежними;
- Боб и Вера не изменились, потому что их не пропустило условие `WHERE id = 1`.

`UPDATE` не переписывает всю таблицу с нуля. Он меняет только то, что ты попросил.