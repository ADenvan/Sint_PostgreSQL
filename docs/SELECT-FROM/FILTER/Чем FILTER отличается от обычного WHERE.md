
## Чем FILTER отличается от обычного WHERE

Это очень важный момент.

Обычный `WHERE` фильтрует строки для всего запроса.

Например:

```sql
SELECT
  COUNT(*) AS orders_total
FROM orders
WHERE status = 'paid';
```

Такой запрос сначала оставит только оплаченные заказы, а потом посчитает их.

То есть все остальные строки вообще не попадут в расчёт.

А `FILTER` работает точечно, только для одного агрегата.

```sql
SELECT
  COUNT(*) AS orders_total,
  COUNT(*) FILTER (WHERE status = 'paid') AS paid_orders
FROM orders;
```

Здесь:

```sql
COUNT(*) AS orders_total
```

считает все строки.

А:

```sql
COUNT(*) FILTER (WHERE status = 'paid') AS paid_orders
```

считает только оплаченные строки.

То есть общий `WHERE` отвечает за входные данные всего запроса, а `FILTER` — за условие внутри конкретной метрики.

Можно запомнить так:

> `WHERE` фильтрует строки для всего запроса. `FILTER` фильтрует строки только для одного агрегата.

## Пример: выручка по статусам

Теперь посчитаем не только количество заказов, но и сумму.

Допустим, в таблице `orders` есть суммы заказов:

```text
id | amount | status
---+--------+----------
1  | 1500   | paid
2  | 2300   | paid
3  | 900    | refunded
4  | 700    | failed
5  | 1200   | paid
```

Хотим получить:

- общую сумму всех заказов;
- выручку по оплаченным заказам;
- сумму возвратов;
- сумму неуспешных заказов.

```sql
SELECT
  SUM(amount) AS amount_total,
  SUM(amount) FILTER (WHERE status = 'paid') AS revenue_paid,
  SUM(amount) FILTER (WHERE status = 'refunded') AS amount_refunded,
  SUM(amount) FILTER (WHERE status = 'failed') AS amount_failed
FROM orders;
```

Результат:

```text
amount_total | revenue_paid | amount_refunded | amount_failed
-------------+--------------+-----------------+--------------
6600         | 5000         | 900             | 700
```

`SUM(amount)` считает сумму по всем строкам.

А:

```sql
SUM(amount) FILTER (WHERE status = 'paid')
```

считает сумму только по оплаченным заказам.

Это очень удобно: в одном запросе можно собрать целый блок метрик для отчёта.

## Пример: несколько метрик по дням

`FILTER` особенно полезен вместе с `GROUP BY`.

Допустим, мы хотим построить отчёт по дням:

- всего заказов за день;
- оплаченных заказов;
- возвращённых заказов;
- выручку по оплаченным заказам.

```sql
SELECT
  DATE_TRUNC('day', created_at) AS day,
  COUNT(*) AS orders_total,
  COUNT(*) FILTER (WHERE status = 'paid') AS paid_orders,
  COUNT(*) FILTER (WHERE status = 'refunded') AS refunded_orders,
  SUM(amount) FILTER (WHERE status = 'paid') AS revenue_paid
FROM orders
GROUP BY DATE_TRUNC('day', created_at)
ORDER BY day;
```

Результат может быть таким:

```text
day                  | orders_total | paid_orders | refunded_orders | revenue_paid
---------------------+--------------+-------------+-----------------+-------------
2026-06-17 00:00:00  | 10           | 7           | 1               | 12500
2026-06-18 00:00:00  | 8            | 5           | 2               | 9300
```

Здесь каждая строка результата — отдельный день.

А внутри каждого дня агрегаты считают разные сегменты:

- `COUNT(*)` — все заказы;
- `COUNT(*) FILTER (WHERE status = 'paid')` — только оплаченные;
- `COUNT(*) FILTER (WHERE status = 'refunded')` — только возвраты;
- `SUM(amount) FILTER (WHERE status = 'paid')` — выручку только по оплаченным заказам.

Такой запрос хорошо подходит для графиков и дашбордов.

## Пример: метрики по странам

Теперь пример посложнее.

Есть таблица `users`:

```text
id | email          | country
---+----------------+---------
1  | anna@mail.com  | Vietnam
2  | bob@mail.com   | Vietnam
3  | kate@mail.com  | Germany
```

И таблица `orders`:

```text
id | user_id | amount | status
---+---------+--------+--------
1  | 1       | 1500   | paid
2  | 1       | 2300   | paid
3  | 2       | 900    | failed
```

Хотим получить отчёт по странам:

- сколько всего пользователей;
- сколько пользователей сделали хотя бы один заказ;
- сколько оплаченных заказов;
- какая оплаченная выручка;
- какой средний оплаченный чек.

Запрос:

```sql
SELECT
  u.country,
  COUNT(DISTINCT u.id) AS users_total,
  COUNT(DISTINCT u.id) FILTER (WHERE o.id IS NOT NULL) AS users_with_orders,
  COUNT(*) FILTER (WHERE o.status = 'paid') AS paid_orders,
  COALESCE(SUM(o.amount) FILTER (WHERE o.status = 'paid'), 0) AS revenue_paid,
  AVG(o.amount) FILTER (WHERE o.status = 'paid') AS avg_paid_order
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.country
ORDER BY u.country;
```

Здесь есть важная тонкость.

После `LEFT JOIN` один пользователь может превратиться в несколько строк, если у него несколько заказов.

Например, если у пользователя Anna два заказа, после соединения она будет встречаться два раза.

Поэтому для подсчёта пользователей безопаснее писать:

```sql
COUNT(DISTINCT u.id)
```

А не просто:

```sql
COUNT(*)
```

Иначе количество пользователей может случайно раздуться из-за заказов.

Разберём метрики:

```sql
COUNT(DISTINCT u.id) AS users_total
```

считает всех уникальных пользователей в стране.

```sql
COUNT(DISTINCT u.id) FILTER (WHERE o.id IS NOT NULL) AS users_with_orders
```

считает уникальных пользователей, у которых есть хотя бы один заказ.

```sql
COUNT(*) FILTER (WHERE o.status = 'paid') AS paid_orders
```

считает количество оплаченных заказов.

```sql
SUM(o.amount) FILTER (WHERE o.status = 'paid') AS revenue_paid
```

считает сумму только по оплаченным заказам.

```sql
AVG(o.amount) FILTER (WHERE o.status = 'paid') AS avg_paid_order
```

считает средний чек только по оплаченным заказам.

Такой подход позволяет собрать несколько связанных метрик в одном понятном запросе.