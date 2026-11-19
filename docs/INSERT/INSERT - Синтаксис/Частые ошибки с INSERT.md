
## Частые ошибки с INSERT

### Не указывать список колонок

Плохой вариант:
```sql
INSERT INTO users
VALUES ('alice@example.com', 'Alice', 'RU');
```

Хороший вариант:
```sql
INSERT INTO users (email, display_name, country)
VALUES ('alice@example.com', 'Alice', 'RU');
```
Список колонок делает запрос понятным и устойчивым к изменениям таблицы.

### Перепутать порядок значений

Такой запрос формально может выглядеть нормально, но данные попадут не туда:
```sql
INSERT INTO users (email, display_name, country)
VALUES ('Alice', 'alice@example.com', 'RU');
```

База не всегда поймёт, что ты перепутал email и имя. Она просто вставит строки в указанном порядке.

Правильно:
```sql
INSERT INTO users (email, display_name, country)
VALUES ('alice@example.com', 'Alice', 'RU');
```

Сначала колонка `email` — значит, сначала значение email. Потом `display_name` — значит, потом имя.

### Передать не то количество значений

Если указали три колонки, значений тоже должно быть три.
```sql
INSERT INTO users (email, display_name, country)
VALUES ('alice@example.com', 'Alice');
```

Здесь три колонки, но только два значения. База выдаст ошибку.

Правильно:
```sql
INSERT INTO users (email, display_name, country)
VALUES ('alice@example.com', 'Alice', 'RU');
```

### Использовать двойные кавычки для строк

В SQL строки пишутся в одинарных кавычках.

Правильно:

```sql
INSERT INTO users (display_name)
VALUES ('Alice');
```

Неправильно:

```sql
INSERT INTO users (display_name)
VALUES ("Alice");
```

В PostgreSQL двойные кавычки используются для имён таблиц и колонок, а не для строковых значений. Поэтому база может решить, что `"Alice"` — это имя колонки.

### Вставлять id вручную без необходимости

Почти всегда лучше так:

```sql
INSERT INTO users (email, display_name)
VALUES ('alice@example.com', 'Alice');
```

А не так:

```sql
INSERT INTO users (id, email, display_name)
VALUES (1, 'alice@example.com', 'Alice');
```

Если `id` генерируется автоматически, пусть база сама его выдаёт.

Ручная вставка `id` может привести к конфликтам и путанице с последовательностью автоинкремента.

### Делать слишком огромный INSERT

Технически можно попытаться вставить гигантскую пачку одним запросом. Но это не всегда хорошая идея.

Большой `INSERT` может:

- раздуть WAL-журнал;
- создать долгую транзакцию;
- задержать репликацию;
- сильнее нагрузить индексы;
- усложнить откат при ошибке.

Для больших загрузок лучше использовать разумные batch-вставки или специальные инструменты вроде `COPY`.