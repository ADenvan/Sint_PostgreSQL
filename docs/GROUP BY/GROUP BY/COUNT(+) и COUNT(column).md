
## COUNT(*) и COUNT(column)

Это важная тема, потому что новички часто думают, что `COUNT(*)` и `COUNT(email)` делают одно и то же.

На самом деле нет.

`COUNT(*)` считает все строки в группе.

`COUNT(column)` считает только строки, где в этой колонке не `NULL`.

Пример:

|id|country|email|
|--:|---|---|
|1|RU|[a@example.com](mailto:a@example.com)|
|2|RU|NULL|
|3|RU|[c@example.com](mailto:c@example.com)|
|4|US|NULL|
|5|US|[e@example.com](mailto:e@example.com)|

Запрос:

```sql
SELECT
  country,
  COUNT(*) AS rows_count,
  COUNT(email) AS emails_count
FROM users
GROUP BY country;
```

Результат:

|country|rows_count|emails_count|
|---|--:|--:|
|RU|3|2|
|US|2|1|

Для `RU` всего 3 строки, но email есть только у 2 пользователей.

Поэтому:

- если нужно посчитать строки — используй `COUNT(*)`;
- если нужно посчитать заполненные значения в колонке — используй `COUNT(column)`.