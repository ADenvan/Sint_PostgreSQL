
## `ELSE`: что вернуть, если ничего не подошло

Часть `ELSE` отвечает за запасной вариант.

```sql
CASE
  WHEN total_spent >= 10000 THEN 'platinum'
  WHEN total_spent >= 1000 THEN 'gold'
  WHEN total_spent >= 100 THEN 'silver'
  ELSE 'bronze'
END
```

Если ни одно условие не сработало, SQL вернёт `bronze`.

А что будет, если `ELSE` не написать?

```sql
SELECT
  name,
  total_spent,
  CASE
    WHEN total_spent >= 10000 THEN 'platinum'
    WHEN total_spent >= 1000 THEN 'gold'
    WHEN total_spent >= 100 THEN 'silver'
  END AS tier
FROM users;
```

Если у пользователя `total_spent = 50`, ни одно условие не выполнится. В результате будет `NULL`.

Это не всегда ошибка. Иногда `NULL` действительно означает «категория не определена». Но в отчётах такие пустоты часто выглядят странно.

Поэтому хорошая привычка для новичка: почти всегда добавлять `ELSE`.