
## COUNT - посчитать строки

`COUNT` отвечает на вопрос «сколько?».

Самый частый вариант — `COUNT(*)`:

```sql
SELECT COUNT(*) AS users_count
FROM users;
```

Он считает количество строк в таблице.

Например, есть таблица `users`:

|id|name|email|
|--:|---|---|
|1|Anna|[anna@example.com](mailto:anna@example.com)|
|2|Bob|NULL|
|3|Vera|[vera@example.com](mailto:vera@example.com)|
|4|Bob|[bob@example.com](mailto:bob@example.com)|

Запрос:

```sql
SELECT COUNT(*) AS all_rows
FROM users;
```

Вернёт:

|all_rows|
|--:|
|4|

Потому что в таблице четыре строки.