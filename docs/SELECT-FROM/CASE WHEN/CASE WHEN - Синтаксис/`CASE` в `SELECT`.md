
## `CASE` в `SELECT`

Самое частое место для `CASE` — список колонок в `SELECT`.
Например, хотим вывести пользователей и подписать, активны они или нет:

```sql
SELECT
  id,
  email,
  CASE
    WHEN last_login_at >= CURRENT_DATE - INTERVAL '30 days' THEN 'active'
    ELSE 'inactive'
  END AS activity_status
FROM users;
```

В таблице может не быть колонки `activity_status`. Мы создаём её на лету.

Это удобно для витрин, аналитики, админок и выгрузок: база сразу возвращает не просто даты, суммы и флаги, а понятные категории.