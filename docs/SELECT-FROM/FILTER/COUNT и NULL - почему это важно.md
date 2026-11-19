
## COUNT и NULL: почему это важно

С агрегатами важно помнить, как они работают с `NULL`.

`COUNT(*)` считает строки.

```sql
COUNT(*)
```

А `COUNT(column)` считает только строки, где `column` не `NULL`.

Например:

```text
id | amount
---+--------
1  | 100
2  | NULL
3  | 300
```

```sql
SELECT
  COUNT(*) AS rows_count,
  COUNT(amount) AS amount_count
FROM orders;
```

Результат:

```text
rows_count | amount_count
-----------+-------------
3          | 2
```

Почему `amount_count = 2`?

Потому что `COUNT(amount)` не считает строку, где `amount` равен `NULL`.

С `FILTER` это тоже важно.

Например:

```sql
COUNT(amount) FILTER (WHERE status = 'paid')
```

посчитает только оплаченные строки, где `amount` не `NULL`.

А:

```sql
COUNT(*) FILTER (WHERE status = 'paid')
```

посчитает все оплаченные строки, даже если в каких-то из них `amount` равен `NULL`.

Для количества заказов чаще нужен `COUNT(*)`.

Для количества заполненных значений в колонке — `COUNT(column)`.