
## Базовый синтаксис INSERT

Посмотрим на обычную вставку пользователя:

```sql
INSERT INTO users (email, display_name, country)
VALUES ('alice@example.com', 'Alice', 'RU');
```

Разберём по частям.

`INSERT INTO users` говорит базе: вставляем данные в таблицу `users`.
`(email, display_name, country)` — это список колонок, которые мы хотим заполнить.
`VALUES (...)` — это значения для этих колонок. Очень важно: значения идут **в том же порядке**, что и колонки.

То есть здесь:

```sql
(email, display_name, country)
```

соответствует:

```sql
('alice@example.com', 'Alice', 'RU')
```

Получается:

|Колонка|Значение|
|---|---|
|`email`|`alice@example.com`|
|`display_name`|`Alice`|
|`country`|`RU`|

Главное правило для новичка: **всегда указывай список колонок явно**.

Плохо писать так:

```sql
INSERT INTO users
VALUES ('alice@example.com', 'Alice', 'RU');
```

На первый взгляд короче. Но такой запрос зависит от порядка колонок в таблице. Сегодня он работает, а завтра кто-то добавит новую колонку через `ALTER TABLE`, и старый код внезапно сломается.

Хорошая привычка:

```sql
INSERT INTO users (email, display_name, country)
VALUES ('alice@example.com', 'Alice', 'RU');
```

Так запрос читается понятнее и переживает изменения таблицы гораздо спокойнее.

## Пример с таблицей

Допустим, у нас есть пустая таблица `users`.

|id|email|display_name|country|
|--:|---|---|---|
|_нет строк_||||

Добавим первого пользователя:

```sql
INSERT INTO users (email, display_name, country)
VALUES ('anya@example.com', 'Anya', 'RU');
```

После вставки таблица может выглядеть так:

|id|email|display_name|country|
|--:|---|---|---|
|1|[anya@example.com](mailto:anya@example.com)|Anya|RU|

Обрати внимание: в запросе мы не передавали `id`, но он появился сам.

Так часто делают в таблицах: колонка `id` создаётся как автоинкрементная. В PostgreSQL для этого могут использоваться `SERIAL`, `BIGSERIAL` или `IDENTITY`. База сама выдаёт следующий номер: первой строке `1`, второй `2`, третьей `3`.

Поэтому обычно `id` руками не вставляют. Это работа базы данных.