
## Условные суммы через `CASE`

Через `CASE` можно считать не только количество, но и суммы.
Например, хотим посчитать выручку по статусам заказов:

```sql
SELECT
  SUM(CASE WHEN status = 'paid' THEN amount ELSE 0 END) AS paid_amount,
  SUM(CASE WHEN status = 'refunded' THEN amount ELSE 0 END) AS refunded_amount,
  SUM(CASE WHEN status = 'cancelled' THEN amount ELSE 0 END) AS cancelled_amount
FROM orders;
```

Здесь каждая сумма берёт только нужные строки.
Для оплаченных заказов:

```sql
CASE WHEN status = 'paid' THEN amount ELSE 0 END
```

Если заказ оплачен — берём его сумму.
Если нет — подставляем 0.
Потом `SUM` складывает всё в одну итоговую цифру.
Это очень частый приём в финансовых отчётах.