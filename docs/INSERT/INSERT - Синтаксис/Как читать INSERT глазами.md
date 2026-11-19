
## Как читать INSERT глазами

Когда видишь запрос:
```sql
INSERT INTO orders (customer_id, amount, status)
VALUES (7, 250, 'new')
RETURNING id;
```

читай его так:

> «В таблицу `orders` добавь новую строку. В колонку `customer_id` положи `7`, в `amount` — `250`, в `status` — `new`. После вставки верни `id`, который база выдала этой строке».

А такой запрос:
```sql
INSERT INTO users (email, display_name, last_login_at)
VALUES ('alice@example.com', 'Alice', NOW())
ON CONFLICT (email) DO UPDATE
SET last_login_at = EXCLUDED.last_login_at;
```

читай так:

>«Попробуй добавить пользователя. Если пользователь с таким email уже есть, не падай с ошибкой, а обнови ему дату последнего входа».

Когда начинаешь читать SQL таким образом, запросы перестают выглядеть как магические заклинания. Они становятся обычными инструкциями для базы данных.