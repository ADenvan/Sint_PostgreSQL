
## Типы данных в `COALESCE`

Все аргументы `COALESCE` должны быть совместимы по типам.

Хороший пример:

```sql
SELECT COALESCE(nickname, full_name, 'Guest') AS display_name
FROM users;
```

Здесь все значения текстовые.

Тоже хороший пример:

```sql
SELECT COALESCE(points, 0) AS points
FROM users;
```

Здесь `points` — число, и 0 — число.

А вот так может быть ошибка:

```sql
SELECT COALESCE(points, 'unknown') AS points_label
FROM users;
```

Если `points` — числовая колонка, а `unknown` — текст, базе нужно решить, какой тип должен быть у результата. В PostgreSQL такой запрос может закончиться ошибкой преобразования типов.

Правильнее явно выбрать одну идею.

Если нужен числовой результат:

```sql
SELECT COALESCE(points, 0) AS points
FROM users;
```

Если нужен текстовый результат:

```sql
SELECT COALESCE(points::TEXT, 'unknown') AS points_label
FROM users;
```

Главное: не смешивать в одной функции числа, даты и текст без понимания, к чему база будет приводить типы.