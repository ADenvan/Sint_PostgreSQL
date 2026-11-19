
## Короткая шпаргалка `UPDATE`

| Часть запроса        | За что отвечает               |
| -------------------- | ----------------------------- |
| `UPDATE users`       | Какую таблицу обновляем       |
| `SET tier = 'gold'`  | Какую колонку и на что меняем |
| `WHERE id = 1`       | Какие строки обновляем        |
| `RETURNING id, tier` | Что показать после обновления |

Пример целиком:
```sql
UPDATE users
SET
  tier = 'gold',
  upgraded_at = NOW()
WHERE id = 1
RETURNING id, tier, upgraded_at;
```