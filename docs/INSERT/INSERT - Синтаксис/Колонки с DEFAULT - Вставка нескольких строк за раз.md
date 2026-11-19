
## Колонки с DEFAULT

У таблицы могут быть колонки со значением по умолчанию.

Например:

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL,
  display_name TEXT NOT NULL,
  country TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

Колонка `created_at` получает значение автоматически: если мы её не указали, PostgreSQL сам подставит текущее время.

Поэтому такой запрос нормальный:

```sql
INSERT INTO users (email, display_name, country)
VALUES ('bob@example.com', 'Bob', 'US');
```

В таблицу попадут email, имя, страна, а `id` и `created_at` база заполнит сама.

Это удобно: приложению не нужно каждый раз думать, какой следующий `id` и какую дату регистрации поставить.

## Вставка нескольких строк за раз

Иногда нужно добавить не одну строку, а сразу несколько. Например, загрузить список пользователей, товаров или справочников.

Можно сделать три отдельных запроса:

```sql
INSERT INTO users (email, display_name, country)
VALUES ('anya@example.com', 'Anya', 'RU');

INSERT INTO users (email, display_name, country)
VALUES ('bob@example.com', 'Bob', 'US');

INSERT INTO users (email, display_name, country)
VALUES ('vera@example.com', 'Vera', 'BY');
```

Но лучше вставить всё одним запросом:

```sql
INSERT INTO users (email, display_name, country)
VALUES
  ('anya@example.com', 'Anya', 'RU'),
  ('bob@example.com', 'Bob', 'US'),
  ('vera@example.com', 'Vera', 'BY');
```

Это называется batch-вставка, то есть вставка пачкой.

Почему так лучше?

База получает один запрос вместо трёх. Меньше сетевых походов между приложением и сервером. Индексы обновляются эффективнее. Вся пачка вставляется как одна операция.

Если строк много, разница становится заметной. На практике данные часто грузят пачками по 1000–10000 строк, но точный размер зависит от базы, таблицы, индексов, ограничений и нагрузки.

Главная мысль простая: если нужно вставить много строк, не отправляй по одному `INSERT` на каждую строку без необходимости. Пачки почти всегда быстрее.