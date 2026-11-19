
### Думать, что OFFSET сразу прыгает к нужной строке

Запрос с большим `OFFSET` может быть медленным.

```sql
SELECT id, name
FROM products
ORDER BY id
LIMIT 20 OFFSET 1000000;
```

Для глубоких страниц лучше подумать о keyset-пагинации.