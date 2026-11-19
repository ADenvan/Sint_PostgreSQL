
## ON DELETE CASCADE

`DELETE` может удалить не только одну строку, но и запустить удаление связанных строк, если так настроены внешние ключи.

Допустим, есть покупатели и заказы.
```sql
CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL UNIQUE
);
```

Создадим таблицу заказов:

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_id INT NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
  amount NUMERIC(12, 2) NOT NULL
);
```

Здесь важная часть:

```sql
REFERENCES customers(id) ON DELETE CASCADE
```

Она означает:

> Если удалить покупателя, автоматически удали его заказы.

Теперь такой запрос:
```sql
DELETE FROM customers
WHERE id = 5;
```
может удалить не только строку из `customers`, но и все строки из `orders`, где `customer_id = 5`.

Это удобно, когда дочерние данные не имеют смысла без родительской строки.

Например:
- удалить пост и все его комментарии;
- удалить корзину и все её элементы;
- удалить черновик и все связанные временные данные.

Но это опасно, если вы не ожидаете каскадного удаления.

Удалили одну строку — а вместе с ней улетели десятки, тысячи или миллионы связанных строк.