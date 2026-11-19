
## GROUP BY по нескольким колонкам

Группировать можно не только по одной колонке.

Например, у пользователей есть страна и тариф:

|id|country|tier|
|--:|---|---|
|1|RU|free|
|2|RU|paid|
|3|RU|free|
|4|US|free|
|5|US|paid|
|6|US|paid|

Можно посчитать пользователей по каждой паре `country` + `tier`:

```sql
SELECT
  country,
  tier,
  COUNT(*) AS users_count
FROM users
GROUP BY country, tier
ORDER BY country, tier;
```

Результат:

|country|tier|users_count|
|---|---|--:|
|RU|free|2|
|RU|paid|1|
|US|free|1|
|US|paid|2|

Здесь группа — это не просто страна. Группа — это комбинация значений.

То есть:

- `RU` + `free` — одна группа;
- `RU` + `paid` — другая группа;
- `US` + `free` — третья группа;
- `US` + `paid` — четвёртая группа.

Простое правило:

> Чем больше колонок в `GROUP BY`, тем подробнее становится группировка.