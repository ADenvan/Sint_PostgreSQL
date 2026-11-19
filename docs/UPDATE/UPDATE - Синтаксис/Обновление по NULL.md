
## Обновление по NULL

С `NULL` в SQL всегда нужно быть аккуратным.

Если нужно найти строки, где значение отсутствует, нельзя писать так:
```sql
UPDATE users
SET email_confirmed = FALSE
WHERE email = NULL;
```
Такой запрос не сработает как ожидается.

Для `NULL` используют `IS NULL`:
```sql
UPDATE users
SET email_confirmed = FALSE
WHERE email IS NULL;
```

А если нужно обновить строки, где значение есть:

```sql
UPDATE users
SET email_confirmed = TRUE
WHERE email IS NOT NULL;
```

Запомни: `NULL` — это не обычное значение. Это «значения нет». Поэтому сравнения через `=` здесь не подходят.