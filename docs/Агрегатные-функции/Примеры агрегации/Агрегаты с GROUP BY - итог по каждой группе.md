
## Агрегаты с `GROUP BY`: итог по каждой группе

Но чаще в отчётах нужно получить не один общий итог, а итоги по группам.

Например:

- сколько товаров в каждой категории;
- сколько заказов сделал каждый клиент;
- какая средняя оценка у каждого товара;
- сколько денег пришло в каждый день.

Для этого нужен `GROUP BY`.

Допустим, есть товары:

|id|category|price|
|--:|---|--:|
|1|books|700|
|2|books|1200|
|3|games|3000|
|4|games|2500|
|5|devices|9000|

Запрос:

```sql
SELECT
  category,
  COUNT(*) AS items_count,
  SUM(price) AS total_price,
  AVG(price) AS avg_price,
  MIN(price) AS min_price,
  MAX(price) AS max_price
FROM products
GROUP BY category;
```

Результат:

|category|items_count|total_price|avg_price|min_price|max_price|
|---|--:|--:|--:|--:|--:|
|books|2|1900|950|700|1200|
|games|2|5500|2750|2500|3000|
|devices|1|9000|9000|9000|9000|

Теперь каждая категория получила свою строку с итогами.

`GROUP BY category` означает: «разбей строки на группы по категории и посчитай агрегаты отдельно для каждой группы».