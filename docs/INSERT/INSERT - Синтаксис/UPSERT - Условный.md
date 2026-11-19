
## Условный UPSERT

Иногда обновлять строку нужно не всегда.
Например, мы хотим обновить `last_login_at` только если новое время свежее старого.
^i4
```sql
INSERT INTO users (email, display_name, last_login_at)
VALUES ('anya@example.com', 'Anya', '2026-06-26 10:00:00')
ON CONFLICT (email) DO UPDATE
SET
  last_login_at = EXCLUDED.last_login_at,
  display_name = EXCLUDED.display_name
WHERE users.last_login_at < EXCLUDED.last_login_at;
```

^e63cf9

Так база не перетрёт свежие данные более старыми.
Это полезно при импортах, синхронизациях и повторной обработке событий, когда данные могут приходить не строго по порядку.