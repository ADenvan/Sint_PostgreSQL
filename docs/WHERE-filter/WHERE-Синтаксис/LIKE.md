
## LIKE: поиск по шаблону

`LIKE` используют для поиска по тексту, когда нужно не точное совпадение, а шаблон.

Например, найти пользователей с почтой на Gmail:

```sql
SELECT id, email
FROM users
WHERE email LIKE '%@gmail.com';
```

Символ `%` означает «любое количество любых символов».

То есть шаблон `'%@gmail.com'` подходит для:

|email|
|---|
|[alice@gmail.com](mailto:alice@gmail.com)|
|[bob@gmail.com](mailto:bob@gmail.com)|
|[support.team@gmail.com](mailto:support.team@gmail.com)|

Ещё примеры:

```sql
SELECT id, name
FROM users
WHERE name LIKE 'A%';
```

Имена, которые начинаются на `A`.

```sql
SELECT id, name
FROM users
WHERE name LIKE '%ann%';
```

Имена, где внутри есть `ann`.