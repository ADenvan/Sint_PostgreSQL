
## Базовый синтаксис `COALESCE`

Синтаксис простой:

```sql
COALESCE(value_1, value_2, value_3)
```

Аргументов может быть два, три, пять — сколько нужно.
SQL проверяет их слева направо и возвращает первое значение, которое не равно `NULL`.

Например:

```sql
SELECT COALESCE(NULL, NULL, 'hello', 'world') AS result;
```

Результат:

|result|
|---|
|hello|

Почему вернулся `hello`?
Потому что первые два значения — `NULL`, а `hello` — первое нормальное значение.
До `world` дело уже не дошло.
Если все значения равны `NULL`, результат тоже будет `NULL`:

```sql
SELECT COALESCE(NULL, NULL, NULL) AS result;
```

Результат:

|result|
|---|
|NULL|

## Пример с пользователями

Допустим, есть таблица `users`:

|id|full_name|nickname|
|--:|---|---|
|1|Anna|anya_88|
|2|Bob|NULL|
|3|NULL|gigachad|
|4|NULL|NULL|

Нужно вывести имя, которое можно показать в интерфейсе.
Логика такая:
- если есть `nickname`, показываем его;
- если `nickname` нет, показываем `full_name`;
- если нет ни того ни другого, показываем гостевое имя.

Запрос:

```sql
SELECT
  id,
  COALESCE(nickname, full_name, 'Guest') AS display_name
FROM users;
```

Результат:

|id|display_name|
|--:|---|
|1|anya_88|
|2|Bob|
|3|gigachad|
|4|Guest|

Разберём по строкам.

У первого пользователя есть `nickname`, поэтому вернулся `anya_88`.
У второго `nickname` равен `NULL`, зато есть `full_name`, поэтому вернулся `Bob`.
У третьего нет `full_name`, но есть `nickname`, поэтому вернулся `gigachad`.
У четвёртого оба поля равны `NULL`, поэтому сработал последний запасной вариант — `Guest`.
В этом и красота `COALESCE`: он позволяет написать цепочку fallback-значений прямо в запросе.