
## ORDER BY после GROUP BY

`ORDER BY` часто используют вместе с группировкой.

Например, нужно посчитать выручку по каждому пользователю и отсортировать клиентов по сумме покупок:

```sql
SELECT
  customer_id,
  SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id
ORDER BY total_amount DESC;
```

Для каждого региона посчитайте суммарное население как сумму `population` по всем его городам. Регионы, в которых нет ни одного города, в результат не включайте. Отсортируйте результат так, чтобы самые населённые регионы были сверху.
```sql
SELECT 
    r.name AS region_name, 
    SUM(c.population) AS total_population
FROM regions r
JOIN cities c ON r.id = c.region_id
GROUP BY r.name
ORDER BY total_population DESC;
```

Здесь происходит несколько шагов:

1. `GROUP BY customer_id` собирает заказы по клиентам.
2. `SUM(amount)` считает сумму заказов каждого клиента.
3. `ORDER BY total_amount DESC` ставит клиентов с самой большой суммой наверх.

Так получаются рейтинги, топы и отчёты.

Ещё пример: найти самые активные категории товаров.

```sql
SELECT
  category_id,
  COUNT(*) AS products_count
FROM products
GROUP BY category_id
ORDER BY products_count DESC;
```

Сначала считаем количество товаров в каждой категории, потом сортируем категории по этому количеству.

---
Для каждого региона посчитайте суммарное население как сумму `population` по всем его городам. Регионы, в которых нет ни одного города, в результат не включайте. Отсортируйте результат так, чтобы самые населённые регионы были сверху.
```sql
SELECT 
    r.name AS region_name, 
    SUM(c.population) AS total_population
FROM regions r
JOIN cities c ON r.id = c.region_id
GROUP BY r.name
ORDER BY total_population DESC;
```
## Разбор того, что мы добавили (по шагам):

1. **`SUM(c.population)`** — это агрегатная функция. Она говорит базе: _"Не показывай мне население каждого города по отдельности, а сложи все значения `population` вместе"_.
2. **`GROUP BY r.name`** — это **железное правило SQL**: если ты используешь агрегатную функцию (как `SUM`), то все остальные колонки в `SELECT`, которые не обернуты в функцию, обязаны быть в `GROUP BY`. Это говорит базе: _"Сначала раздели все строки на группы по имени региона, а потом посчитай сумму внутри каждой группы"_.
3. **`AS region_name` и `AS total_population`** — это алиасы (псевдонимы). Мы переименовываем колонки на лету, чтобы они точно совпадали с требуемым форматом ответа (`region_name` и `total_population`).
4. **`ORDER BY total_population DESC`** — сортирует итоговый результат по убыванию (`DESC` = descending), чтобы самые населенные регионы оказались наверху, как в примере.