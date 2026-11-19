
## Длинные цепочки `COALESCE`

`COALESCE` может принимать много аргументов:

```sql
SELECT COALESCE(phone, mobile_phone, work_phone, email, 'no_contact') AS contact
FROM users;
```

Иногда это нормально. Например, мы действительно выбираем первый доступный способ связи.
Но если цепочка становится слишком длинной, это повод задуматься.

```sql
COALESCE(a, b, c, d, e, f, g)
```

Формально работает, но читать такое тяжело. Часто длинная цепочка говорит о том, что данные хранятся не очень удобно или в схеме накопилось много исторических полей.

Для новичка важна простая мысль: `COALESCE` помогает аккуратно обработать `NULL`, но не должен маскировать хаос в данных.

## Практический пример: карточка пользователя

Допустим, нужно собрать данные для карточки пользователя.

Таблица `users`:

|id|nickname|full_name|email|points|
|--:|---|---|---|--:|
|1|anya_88|Anna Ivanova|[anna@example.com](mailto:anna@example.com)|120|
|2|NULL|Bob Petrov|[bob@example.com](mailto:bob@example.com)|NULL|
|3|NULL|NULL|[vera@example.com](mailto:vera@example.com)|50|
|4|NULL|NULL|NULL|NULL|

Хотим вывести:

- имя для отображения;
- контакт;
- баллы, где отсутствие баллов считается нулём.

```sql
SELECT
  id,
  COALESCE(nickname, full_name, 'Guest') AS display_name,
  COALESCE(email, 'no_email') AS contact_email,
  COALESCE(points, 0) AS points
FROM users;
```

Результат:

|id|display_name|contact_email|points|
|--:|---|---|--:|
|1|anya_88|[anna@example.com](mailto:anna@example.com)|120|
|2|Bob Petrov|[bob@example.com](mailto:bob@example.com)|0|
|3|Guest|[vera@example.com](mailto:vera@example.com)|50|
|4|Guest|no_email|0|

Такой результат уже можно удобно показывать в интерфейсе. Вместо дыр и пустых значений — понятные fallback-значения.

## Практический пример: отчёт по заказам

Есть таблица `orders`:

|id|customer_id|amount|
|--:|--:|--:|
|1|10|1200|
|2|10|800|
|3|15|500|

Нужно вывести сумму заказов по конкретному клиенту. Если заказов нет — показать 0.

```sql
SELECT
  COALESCE(SUM(amount), 0) AS total_amount
FROM orders
WHERE customer_id = 999;
```

Результат:

|total_amount|
|--:|
|0|

Без `COALESCE` результатом был бы `NULL`.

Для отчёта, где ожидается число, это почти всегда неудобно.