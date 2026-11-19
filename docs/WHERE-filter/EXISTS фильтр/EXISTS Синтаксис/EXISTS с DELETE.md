
## EXISTS с DELETE

`EXISTS` можно использовать и в `DELETE`.

Например, нужно удалить товары, которые есть во временном списке на удаление:

```sql
DELETE FROM products p
WHERE EXISTS (
  SELECT 1
  FROM products_to_delete d
  WHERE d.product_id = p.id
);
```

Или наоборот, удалить записи из временной таблицы, для которых уже нет основного объекта:

```sql
DELETE FROM product_cache pc
WHERE NOT EXISTS (
  SELECT 1
  FROM products p
  WHERE p.id = pc.product_id
);
```

Но с `DELETE` всегда нужно быть осторожным: сначала проверьте условие через `SELECT`.

Например:

```sql
SELECT *
FROM product_cache pc
WHERE NOT EXISTS (
  SELECT 1
  FROM products p
  WHERE p.id = pc.product_id
);
```

И только потом выполняйте удаление.