
## Безопасный алгоритм для UPDATE

Вот простой порядок действий, который стоит запомнить:
1. Сначала напиши `SELECT` с нужным `WHERE`.
2. Проверь, какие строки он возвращает.
3. Убедись, что строк ровно столько, сколько ты ожидаешь.
4. Напиши `UPDATE` с тем же `WHERE`.
5. Если запрос важный, используй транзакцию.
6. После обновления проверь результат.
7. В PostgreSQL по возможности используй `RETURNING`.

Например:
```sql
SELECT
  id,
  email,
  tier
FROM users
WHERE email = 'anya@example.com';
```

Проверили. Теперь обновляем:

```sql
UPDATE users
SET tier = 'gold'
WHERE email = 'anya@example.com'
RETURNING id, email, tier;
```

Так работать спокойнее.