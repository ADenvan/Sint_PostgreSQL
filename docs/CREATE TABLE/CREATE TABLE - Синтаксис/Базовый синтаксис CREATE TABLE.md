
## Базовый синтаксис CREATE TABLE

Посмотрим на пример:
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  display_name VARCHAR(100) NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

Здесь мы создаём таблицу `users` с четырьмя колонками:
- `id` — уникальный идентификатор пользователя;
- `email` — почта пользователя;
- `display_name` — отображаемое имя;
- `created_at` — дата и время создания строки.

Разберём по частям.
```sql
CREATE TABLE users (
  ...
);
```

Так начинается создание таблицы. После `CREATE TABLE` указываем имя таблицы, а внутри скобок перечисляем колонки и правила для них.

```sql
id SERIAL PRIMARY KEY
```

Колонка `id` получает тип `SERIAL`. В PostgreSQL это удобный способ сказать: «пусть база сама выдаёт значения 1, 2, 3, 4 и так далее».

`PRIMARY KEY` означает, что это главный идентификатор строки. Значение должно быть уникальным и не должно быть `NULL`.
```sql
email VARCHAR(255) UNIQUE NOT NULL
```

Колонка `email` хранит текст длиной до 255 символов.

`UNIQUE` запрещает повторения. Два пользователя с одним и тем же email не пройдут.
`NOT NULL` говорит, что email обязателен. Нельзя создать пользователя без email.

```sql
display_name VARCHAR(100) NOT NULL
```

Колонка `display_name` тоже текстовая и тоже обязательная.

```sql
created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
```

Колонка `created_at` хранит дату и время. Тип `TIMESTAMPTZ` в PostgreSQL удобен для событий во времени: регистраций, заказов, оплат, сообщений.

`DEFAULT NOW()` означает: если при вставке строки мы не указали `created_at`, база сама поставит текущий момент.

## Запятые и точка с запятой

Внутри `CREATE TABLE` колонки разделяются запятыми:
```sql
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  price NUMERIC(12, 2) NOT NULL
);
```
После последней колонки запятая обычно не ставится.

В конце всей команды ставится точка с запятой:
```sql
);
```
Это как точка в конце предложения: команда закончилась, можно выполнять.

## Пример из жизни: таблица записей на услугу

Допустим, мы делаем небольшой сервис для записи клиентов. Нужно хранить записи: кто пришёл, какой телефон оставил, какую услугу выбрал и на какое время записался.

Создадим таблицу:
```sql
CREATE TABLE appointments (
  id SERIAL PRIMARY KEY,
  client_name VARCHAR(100) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  service VARCHAR(50) NOT NULL,
  starts_at TIMESTAMPTZ NOT NULL,
  notes TEXT
);
```

Что здесь важно:
- `client_name` — обязательное имя клиента;
- `phone` — обязательный телефон;
- `service` — обязательное название услуги;
- `starts_at` — обязательные дата и время записи;
- `notes` — необязательная заметка.

У `notes` нет `NOT NULL`, значит это поле можно не заполнять. Если заметки нет, в колонке будет `NULL`.

Теперь можно вставить запись:
```sql
INSERT INTO appointments (client_name, phone, service, starts_at)
VALUES ('Anna', '+79991234567', 'haircut', '2026-05-10 14:00:00+03');
```

Результат в таблице будет примерно таким:

|id|client_name|phone|service|starts_at|notes|
|---|---|---|---|---|---|
|1|Anna|+79991234567|haircut|2026-05-10 14:00:00+03|NULL|

Мы не передавали `id`, потому что `SERIAL` сделал это сам.
Мы не передавали `notes`, потому что заметка необязательная.
Так таблица работает как аккуратный бланк: обязательные поля требует, необязательные разрешает пропустить.