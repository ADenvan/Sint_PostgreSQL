
## Частые ошибки новичков

### Думать, что `COALESCE` заменяет пустые строки

Пустая строка не равна `NULL`.

```sql
SELECT COALESCE('', 'default') AS result;
```

Результат — пустая строка.
Если нужно обработать и `NULL`, и пустую строку, используй `NULLIF`:

```sql
SELECT COALESCE(NULLIF(value, ''), 'default') AS result
FROM settings;
```

### Смешивать несовместимые типы

Плохо:

```sql
SELECT COALESCE(points, 'unknown') AS points
FROM users;
```

Если `points` — число, а `unknown` — текст, база может не понять, каким должен быть итоговый тип.

Лучше либо число:

```sql
SELECT COALESCE(points, 0) AS points
FROM users;
```

либо текст:

```sql
SELECT COALESCE(points::TEXT, 'unknown') AS points_label
FROM users;
```

### Использовать `COALESCE` в фильтре там, где достаточно `IS NULL`

Сложнее и хуже для чтения:

```sql
SELECT *
FROM users
WHERE COALESCE(deleted_at, DATE '1970-01-01') = DATE '1970-01-01';
```

Проще:

```sql
SELECT *
FROM users
WHERE deleted_at IS NULL;
```

Для проверки `NULL` в `WHERE` обычно лучше использовать `IS NULL` и `IS NOT NULL`.

### Ждать, что `COALESCE` заменит 0 или `FALSE`

```sql
SELECT COALESCE(0, 100) AS result;
```

Вернёт 0.

```sql
SELECT COALESCE(FALSE, TRUE) AS result;
```

Вернёт `false`.

`COALESCE` реагирует только на `NULL`.
0 и `FALSE` — это нормальные значения.

### Прятать проблему данных за длинной цепочкой

```sql
SELECT COALESCE(a, b, c, d, e, f, 'unknown') AS value
FROM some_table;
```

Иногда это оправдано. Но если таких цепочек много, стоит подумать: почему одно и то же значение может лежать в шести разных колонках?

`COALESCE` помогает сделать вывод аккуратнее, но не заменяет нормальную модель данных.