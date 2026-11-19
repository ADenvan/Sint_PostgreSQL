
## Частые ошибки новичков `UPDATE`

### Забыли WHERE

Самая опасная ошибка:
```sql
UPDATE users
SET tier = 'gold';
```
Такой запрос обновит всех пользователей.

Правильнее:
```sql
UPDATE users
SET tier = 'gold'
WHERE id = 1;
```
Хорошая привычка: как только начал писать `UPDATE`, сразу подумай про `WHERE`.

### Написали слишком широкое условие

Иногда `WHERE` есть, но он слишком общий.

Например:
```sql
UPDATE users
SET promo_code = 'WELCOME10'
WHERE country = 'Russia';
```
Может быть, ты хотел обновить только новых пользователей из России, а обновил вообще всех.

Точнее:
```sql
UPDATE users
SET promo_code = 'WELCOME10'
WHERE country = 'Russia' AND tier = 'free';
```
Перед массовым обновлением всегда полезно сделать проверочный `SELECT`.

### Перепутали одинарные и двойные кавычки

Строки в SQL пишутся в одинарных кавычках.

Правильно:
```sql
UPDATE users
SET name = 'Anna'
WHERE id = 1;
```
В PostgreSQL двойные кавычки используются для имён таблиц и колонок.

Неправильно:
```sql
UPDATE users
SET name = "Anna"
WHERE id = 1;
```
База может решить, что `"Anna"` — это имя колонки, а не строка.

### Забыли запятые в SET

Если обновляешь несколько колонок, между ними нужны запятые.

Неправильно:
```sql
UPDATE users
SET
  tier = 'gold'
  is_verified = TRUE
WHERE id = 1;
```

Правильно:
```sql
UPDATE users
SET
  tier = 'gold',
  is_verified = TRUE
WHERE id = 1;
```

### Используют = NULL

Неправильно:
```sql
UPDATE users
SET email_confirmed = FALSE
WHERE email = NULL;
```

Правильно:
```sql
UPDATE users
SET email_confirmed = FALSE
WHERE email IS NULL;
```
Для `NULL` нужны `IS NULL` и `IS NOT NULL`.

### Считают новое значение в приложении

Опасный подход:
```sql
SELECT points
FROM users
WHERE id = 1;
```

Потом приложение считает новое значение и пишет:

```sql
UPDATE users
SET points = 150
WHERE id = 1;
```
Если параллельно кто-то уже изменил `points`, можно перетереть чужое изменение.

Лучше:
```sql
UPDATE users
SET points = points + 10
WHERE id = 1;
```
База сама возьмёт текущее значение и обновит его.

### Путаются в AND и OR

Сложные условия лучше писать со скобками.

Например:
```sql
UPDATE users
SET bonus = 100
WHERE (country = 'Russia' AND tier = 'gold')
   OR (country = 'Kazakhstan' AND tier = 'gold');
```
Без скобок запрос может читаться не так очевидно. SQL знает приоритеты операторов, но человек легко ошибается.

Скобки делают намерение понятным.