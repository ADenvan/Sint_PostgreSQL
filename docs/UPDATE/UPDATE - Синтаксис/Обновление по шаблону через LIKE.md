
## Обновление по шаблону через LIKE

Можно обновлять строки, где текст подходит под шаблон.

Например, пометить тестовых пользователей:
```sql
UPDATE users
SET is_test = TRUE
WHERE email LIKE '%@test.com';
```
Здесь `%` означает «любое количество любых символов».

То есть условие найдёт email вроде:

|email|
|---|
|[anna@test.com](mailto:anna@test.com)|
|[qa_user@test.com](mailto:qa_user@test.com)|
|[demo@test.com](mailto:demo@test.com)|

Но с такими запросами нужно быть осторожным. Шаблон может оказаться шире, чем ты думаешь. Перед обновлением лучше сделать `SELECT` с тем же условием.
```sql
SELECT
  id,
  email
FROM users
WHERE email LIKE '%@test.com';
```
Сначала посмотрели, потом обновили.