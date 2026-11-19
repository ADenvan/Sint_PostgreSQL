
### Использовать LIMIT без ORDER BY

Плохо:

```sql
SELECT id, title
FROM posts
LIMIT 10;
```

Так ты получишь просто 10 строк. Не топ, не последние, не первые по смыслу.

Хорошо:

```sql
SELECT id, title, created_at
FROM posts
ORDER BY created_at DESC, id DESC
LIMIT 10;
```

Теперь это действительно 10 последних постов.