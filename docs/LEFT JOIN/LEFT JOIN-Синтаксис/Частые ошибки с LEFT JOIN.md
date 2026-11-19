
## Частые ошибки с LEFT JOIN

### Поставить фильтр по правой таблице в WHERE

Плохой вариант:

```sql
SELECT
  u.name,
  o.amount
FROM users AS u
LEFT JOIN orders AS o
  ON u.id = o.user_id
WHERE o.amount > 1000;
```

Так пользователи без заказов исчезнут, потому что `o.amount` у них равен `NULL`.

Если нужно сохранить всех пользователей, а справа подставлять только дорогие заказы, условие нужно перенести в `ON`.

```sql
SELECT
  u.name,
  o.amount
FROM users AS u
LEFT JOIN orders AS o
  ON u.id = o.user_id
 AND o.amount > 1000;
```

### Использовать COUNT(*) вместо COUNT(o.id)

После `LEFT JOIN` такой запрос может обмануть:

```sql
SELECT
  u.name,
  COUNT(*) AS orders_count
FROM users AS u
LEFT JOIN orders AS o
  ON u.id = o.user_id
GROUP BY u.id, u.name;
```

Для пользователя без заказов `COUNT(*)` вернёт `1`.

Правильнее считать реальную колонку заказа:

```sql
SELECT
  u.name,
  COUNT(o.id) AS orders_count
FROM users AS u
LEFT JOIN orders AS o
  ON u.id = o.user_id
GROUP BY u.id, u.name;
```

### Пугаться NULL

`NULL` после `LEFT JOIN` — это нормальный сигнал: справа нет пары.

Если нужно найти такие строки, используй:

```sql
WHERE o.id IS NULL
```

Если нужно красиво вывести ноль вместо пустоты, используй:

```sql
COALESCE(SUM(o.amount), 0)
```

### Использовать LEFT JOIN, когда нужен INNER JOIN

Если нужны только строки с совпадениями, используй `INNER JOIN`.

`LEFT JOIN` нужен не «потому что он мощнее», а потому что задача требует сохранить левую таблицу полностью.

### Не замечать размножение строк

Если справа несколько совпадений, строка слева появится несколько раз.

Это нормально для связей «один ко многим»: один пользователь — много заказов, один пост — много комментариев, один студент — много оценок.

Если нужна одна строка на объект, добавляй агрегаты и `GROUP BY`.