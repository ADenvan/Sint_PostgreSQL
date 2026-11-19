
## `COALESCE` вместо `CASE`

`COALESCE` можно представить как короткую форму `CASE`.

Запрос:

```sql
SELECT COALESCE(nickname, full_name, 'Guest') AS display_name
FROM users;
```

по смыслу похож на:

```sql
SELECT
  CASE
    WHEN nickname IS NOT NULL THEN nickname
    WHEN full_name IS NOT NULL THEN full_name
    ELSE 'Guest'
  END AS display_name
FROM users;
```

Результат будет тот же.

Но `COALESCE` короче и читается лучше, когда логика простая: «возьми первое не `NULL`».
`CASE` нужен, когда условие сложнее.

Например:

```sql
SELECT
  CASE
    WHEN total_spent >= 10000 THEN 'platinum'
    WHEN total_spent >= 1000 THEN 'gold'
    ELSE 'regular'
  END AS user_tier
FROM users;
```

Здесь мы проверяем не `NULL`, а диапазоны значений. Для такой логики нужен `CASE`.

Итого:
- если нужно выбрать первое заполненное значение — `COALESCE`;
- если нужна условная логика — `CASE`.