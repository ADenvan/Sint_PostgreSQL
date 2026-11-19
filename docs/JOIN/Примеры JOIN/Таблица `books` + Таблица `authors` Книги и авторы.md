
## Пример: книги и авторы

Посмотрим на другой пример — библиотеку.

Таблица `books`:

|id|title|author_id|
|--:|---|--:|
|1|War and Peace|10|
|2|Anna Karenina|10|
|3|Crime and Punishment|11|
|4|The Idiot|11|
|5|Unknown Book|99|

Таблица `authors`:

|id|full_name|country|
|--:|---|---|
|10|Leo Tolstoy|Russia|
|11|Fyodor Dostoevsky|Russia|
|12|Erich Maria Remarque|Germany|

Нужно вывести книги вместе с именем автора и страной.

```sql
SELECT
  b.title,
  a.full_name AS author,
  a.country
FROM books b
JOIN authors a
  ON a.id = b.author_id
ORDER BY a.full_name, b.title;
```

Результат:

|title|author|country|
|---|---|---|
|Anna Karenina|Leo Tolstoy|Russia|
|War and Peace|Leo Tolstoy|Russia|
|Crime and Punishment|Fyodor Dostoevsky|Russia|
|The Idiot|Fyodor Dostoevsky|Russia|

Книга `Unknown Book` не попала в результат, потому что у неё `author_id = 99`, а автора с `id = 99` нет в `authors`.

Автор `Erich Maria Remarque` тоже не попал, потому что в таблице `books` у него нет книг.

Так работает `INNER JOIN`: в результате остаются только совпадения.