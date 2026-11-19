
## COUNT(*) и COUNT(column) в HAVING

Важно помнить разницу между `COUNT(*)` и `COUNT(column)`.

`COUNT(*)` считает все строки.

`COUNT(column)` считает только строки, где значение в колонке не `NULL`.

Допустим, есть таблица `users`:

|id|country|email|
|--:|---|---|
|1|RU|[a@example.com](mailto:a@example.com)|
|2|RU|NULL|
|3|RU|[c@example.com](mailto:c@example.com)|
|4|US|NULL|
|5|US|[b@example.com](mailto:b@example.com)|
|6|US|NULL|

Запрос:

```sql
SELECT
  country,
  COUNT(*) AS users_count,
  COUNT(email) AS emails_count
FROM users
GROUP BY country;
```

Результат:

|country|users_count|emails_count|
|---|--:|--:|
|RU|3|2|
|US|3|1|

Теперь посмотрим на `HAVING`.

Если написать так:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
GROUP BY country
HAVING COUNT(*) >= 3;
```

В результат попадут страны, где минимум 3 пользователя.

А если написать так:

```sql
SELECT
  country,
  COUNT(email) AS emails_count
FROM users
GROUP BY country
HAVING COUNT(email) >= 3;
```

В результат не попадёт ни одна страна, потому что ни в `RU`, ни в `US` нет трёх заполненных email.

Поэтому всегда уточняй для себя:

- тебе нужно посчитать строки?
- или только заполненные значения в конкретной колонке?