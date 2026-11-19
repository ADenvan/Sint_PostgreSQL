
# DISTINCT: как убрать дубликаты

Иногда нужно получить не все строки, а только уникальные значения.

Чтобы получить каждый город только один раз, используем `DISTINCT`.
```sql
SELECT DISTINCT city FROM users;
```
Результат:

|city|
|---|
|Moscow|
|Kazan|
|Sochi|

`DISTINCT` убирает дубликаты из результата.

Он может работать и с несколькими колонками:
```sql
SELECT DISTINCT country, city FROM users;
```
В таком случае уникальной считается не одна колонка, а пара значений: `country` плюс `city`.
Например, `Georgia` + `Batumi` и `Georgia` + `Tbilisi` — разные комбинации.

---
По таблице `watch_content` для каждой даты посчитайте общее число просмотров и количество уникальных пользователей. Выведите дневную сводку.

```sql
SELECT DISTINCT watch_date,
  COUNT(video_id) AS views,
  COUNT(DISTINCT user_id) AS audience
FROM watch_content
GROUP BY watch_date
ORDER BY watch_date ASC
```
Результат

|#|watch_date|views|audience|
|---|---|---|---|
|1|2021-01-01|4|2|
|2|2021-01-02|6|3|
|3|2021-01-03|4|3|
|4|2021-01-04|3|3|
