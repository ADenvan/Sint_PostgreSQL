
## `COALESCE` для безопасной арифметики

Один из самых частых сценариев — заменить `NULL` на 0 перед расчётом.
Допустим, есть таблица `users`:

|id|name|points|bonus|
|--:|---|--:|--:|
|1|Anna|100|20|
|2|Bob|50|NULL|
|3|Vera|NULL|10|
|4|Denis|NULL|NULL|

Если написать обычное сложение:

```sql
SELECT
  name,
  points + bonus AS total_score
FROM users;
```

результат будет таким:

|name|total_score|
|---|--:|
|Anna|120|
|Bob|NULL|
|Vera|NULL|
|Denis|NULL|

Почему?

Потому что любое сложение с `NULL` даёт `NULL`.

Для Bob база видит:

```text
50 + unknown = unknown
```

Для Vera:

```text
unknown + 10 = unknown
```

Для Denis:

```text
unknown + unknown = unknown
```

Если по смыслу отсутствующие баллы нужно считать нулём, используем `COALESCE`:

```sql
SELECT
  name,
  COALESCE(points, 0) + COALESCE(bonus, 0) AS total_score
FROM users;
```

Результат:

|name|total_score|
|---|--:|
|Anna|120|
|Bob|50|
|Vera|10|
|Denis|0|

Теперь `NULL` в `points` превращается в 0, и `NULL` в `bonus` тоже превращается в 0.

Это удобно для очков, бонусов, количества товаров, просмотров и других чисел, где пустое значение по бизнес-логике можно считать нулём.