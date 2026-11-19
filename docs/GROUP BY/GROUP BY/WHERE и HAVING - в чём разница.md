
## WHERE и HAVING: в чём разница

`WHERE` и `HAVING` оба фильтруют данные, но делают это в разные моменты.

`WHERE` фильтрует строки до группировки.

`HAVING` фильтрует группы после группировки.

Например, нужно посчитать пользователей по странам, но брать только активных пользователей.

```sql
SELECT
  country,
  COUNT(*) AS active_users_count
FROM users
WHERE status = 'active'
GROUP BY country;
```

Здесь `WHERE status = 'active'` сначала убрал неактивных пользователей, и только потом база сгруппировала оставшиеся строки по странам.

А теперь другая задача: показать только те страны, где активных пользователей больше 100.

```sql
SELECT
  country,
  COUNT(*) AS active_users_count
FROM users
WHERE status = 'active'
GROUP BY country
HAVING COUNT(*) > 100;
```

Здесь:

- `WHERE` оставляет только активных пользователей;
- `GROUP BY` собирает их по странам;
- `HAVING` оставляет только те группы, где `COUNT(*) > 100`.

Плохой вариант:

```sql
SELECT
  country,
  COUNT(*) AS users_count
FROM users
WHERE COUNT(*) > 100
GROUP BY country;
```

Так нельзя, потому что на этапе `WHERE` групп ещё нет. Значит, `COUNT(*)` ещё не посчитан.

Запомнить можно так:

> `WHERE` — фильтр для строк.  
> `HAVING` — фильтр для групп.