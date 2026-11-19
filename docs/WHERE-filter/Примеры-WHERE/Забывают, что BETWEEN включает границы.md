
### Забывают, что BETWEEN включает границы

```sql
SELECT name, price
FROM products
WHERE price BETWEEN 100 AND 500;
```

Этот запрос вернёт товары с ценой `100` и `500` тоже.

Если границы должны быть строгими, пиши явно:

```sql
SELECT name, price
FROM products
WHERE price > 100 AND price < 500;
```