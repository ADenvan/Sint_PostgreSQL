
## NULL в сортировке

`NULL` — это отсутствие значения. И при сортировке с ним нужно быть внимательным.

Например, есть статьи, у части из них есть дата публикации, а часть пока в черновиках:

|id|title|published_at|
|--:|---|---|
|1|SQL SELECT|2024-03-10|
|2|SQL JOIN|NULL|
|3|SQL ORDER BY|2024-03-15|

Если отсортировать по дате, возникает вопрос: куда положить строки с `NULL`? В начало или в конец?

Разные базы данных ведут себя по-разному.

В PostgreSQL:

- при `ASC` значения `NULL` обычно идут в конце;
- при `DESC` значения `NULL` обычно идут в начале.

В MySQL:

- при `ASC` значения `NULL` обычно идут в начале;
- при `DESC` значения `NULL` обычно идут в конце.

Если ты работаешь в PostgreSQL и хочешь явно управлять положением `NULL`, используй `NULLS FIRST` или `NULLS LAST`.

Например, показать сначала опубликованные статьи от свежих к старым, а черновики без даты оставить в конце:

```sql
SELECT title, published_at
FROM articles
ORDER BY published_at DESC NULLS LAST;
```

А если нужно наоборот — строки без даты поднять наверх:

```sql
SELECT title, published_at
FROM articles
ORDER BY published_at DESC NULLS FIRST;
```

В MySQL синтаксиса `NULLS FIRST` и `NULLS LAST` нет. Там часто используют выражение:

```sql
SELECT title, published_at
FROM articles
ORDER BY published_at IS NULL, published_at DESC;
```

`published_at IS NULL` вернёт условный признак: дата отсутствует или нет. Благодаря этому можно управлять тем, куда попадут строки с пустой датой.