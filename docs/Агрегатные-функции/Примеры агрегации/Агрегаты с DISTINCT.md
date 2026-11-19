
## Агрегаты с `DISTINCT`

`DISTINCT` можно использовать не только с `COUNT`.

Например:

```sql
SELECT
  COUNT(DISTINCT customer_id) AS unique_customers,
  SUM(DISTINCT amount) AS sum_unique_amounts
FROM orders;
```

Но на практике чаще всего используют именно:

```sql
SELECT COUNT(DISTINCT customer_id) AS unique_customers
FROM orders;
```

Это понятный и полезный сценарий: посчитать уникальных клиентов.

А вот `SUM(DISTINCT amount)` нужен редко. Он складывает только уникальные суммы заказов, а не все заказы.

Например, если есть три заказа на суммы 100, 100 и 200, то обычный `SUM(amount)` вернёт 400, а `SUM(DISTINCT amount)` вернёт 300.

Чаще бизнесу нужна сумма всех заказов, поэтому с `SUM(DISTINCT ...)` стоит быть осторожнее.