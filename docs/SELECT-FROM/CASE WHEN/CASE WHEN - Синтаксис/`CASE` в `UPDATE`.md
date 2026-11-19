
## `CASE` в `UPDATE`

`CASE` можно использовать и при обновлении данных.

Например, хотим пересчитать уровень пользователя по сумме покупок и записать его в колонку `tier`:

```sql
UPDATE users
SET tier = CASE
  WHEN total_spent >= 10000 THEN 'platinum'
  WHEN total_spent >= 1000 THEN 'gold'
  WHEN total_spent >= 100 THEN 'silver'
  ELSE 'bronze'
END;
```

Здесь `CASE` уже не просто показывает значение в результате. Он помогает записать новое значение в таблицу.

Такой подход полезен для массовых обновлений, когда разные строки должны получить разные значения по одному набору правил.

Например, можно закрыть старые заказы по-разному:

```sql
UPDATE orders
SET status = CASE
  WHEN paid_at IS NOT NULL THEN 'paid'
  WHEN cancelled_at IS NOT NULL THEN 'cancelled'
  ELSE 'pending'
END
WHERE status IS NULL;
```

Каждая строка получит свой статус в зависимости от данных внутри этой строки.