
## Почему нельзя написать агрегат в WHERE

Новички часто пытаются написать так:

```sql
SELECT
  customer_id,
  COUNT(*) AS orders_count
FROM orders
WHERE COUNT(*) > 5
GROUP BY customer_id;
```

Такой запрос неправильный.

Проблема в том, что `WHERE` выполняется до `GROUP BY`. На этом этапе ещё нет групп. А если групп ещё нет, то и `COUNT(*)` ещё не посчитан.

Поэтому условие на агрегат нужно писать в `HAVING`:

```sql
SELECT
  customer_id,
  COUNT(*) AS orders_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 5;
```

Запомнить можно так:

> Если условие про обычную строку — используй `WHERE`.  
> Если условие про результат подсчёта по группе — используй `HAVING`.