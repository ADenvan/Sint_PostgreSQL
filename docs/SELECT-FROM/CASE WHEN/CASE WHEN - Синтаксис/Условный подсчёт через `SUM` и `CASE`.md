
## Условный подсчёт через `SUM` и `CASE`

Один из самых полезных приёмов в аналитике — считать строки по условиям в одном запросе.
Допустим, есть таблица `users`:

|id|country|tier|
|--:|---|---|
|1|USA|free|
|2|USA|gold|
|3|USA|free|
|4|Germany|gold|
|5|Germany|free|

Хотим получить по каждой стране:

- всего пользователей;
- сколько пользователей на бесплатном тарифе;
- сколько пользователей на золотом тарифе.

Можно написать так:

```sql
SELECT
  country,
  COUNT(*) AS total_users,
  SUM(CASE WHEN tier = 'free' THEN 1 ELSE 0 END) AS free_users,
  SUM(CASE WHEN tier = 'gold' THEN 1 ELSE 0 END) AS gold_users
FROM users
GROUP BY country;
```

Как это работает?

Для каждой строки выражение:

```sql
CASE WHEN tier = 'free' THEN 1 ELSE 0 END
```

возвращает 1, если пользователь на тарифе `free`, и 0 в остальных случаях.

Потом `SUM` складывает эти единицы и нули.

Получается счётчик по условию.

Результат:

|country|total_users|free_users|gold_users|
|---|--:|--:|--:|
|Germany|2|1|1|
|USA|3|2|1|

Это похоже на маленькую сводную таблицу прямо в SQL.