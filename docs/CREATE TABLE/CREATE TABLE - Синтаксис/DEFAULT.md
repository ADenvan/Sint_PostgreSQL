
## DEFAULT

`DEFAULT` подставляет значение автоматически, если его не указали в `INSERT`.

Например:
```sql
created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
```

Теперь при вставке строки не нужно каждый раз передавать дату создания.

```sql
INSERT INTO users (email, display_name)
VALUES ('anna@example.com', 'Anna');
```
`created_at` база заполнит сама.

Другой пример:
```sql
status TEXT NOT NULL DEFAULT 'pending'
```

Если при создании заказа статус не указали, заказ станет `pending`.

Это удобно: меньше ручной работы и меньше забытых значений.