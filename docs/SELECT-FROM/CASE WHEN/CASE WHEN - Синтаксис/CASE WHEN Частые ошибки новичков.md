
## Частые ошибки новичков

### Забыть `END`

`CASE` всегда должен заканчиваться словом `END`.

Неправильно:

```sql
SELECT
  CASE
    WHEN score >= 90 THEN 'excellent'
    ELSE 'ok'
  AS result
FROM exams;
```

Правильно:

```sql
SELECT
  CASE
    WHEN score >= 90 THEN 'excellent'
    ELSE 'ok'
  END AS result
FROM exams;
```

`END` закрывает всю конструкцию `CASE`.

### Поставить условия в неправильном порядке

Неправильно:

```sql
SELECT
  score,
  CASE
    WHEN score >= 50 THEN 'ok'
    WHEN score >= 70 THEN 'good'
    WHEN score >= 90 THEN 'excellent'
    ELSE 'failed'
  END AS result
FROM exams;
```

Для `score = 95` результат будет `ok`, потому что первое условие уже сработало.

Правильно:

```sql
SELECT
  score,
  CASE
    WHEN score >= 90 THEN 'excellent'
    WHEN score >= 70 THEN 'good'
    WHEN score >= 50 THEN 'ok'
    ELSE 'failed'
  END AS result
FROM exams;
```

Чем строже условие, тем выше оно обычно стоит.

### Вернуть разные типы в разных ветках

Неправильно:

```sql
SELECT
  CASE
    WHEN amount > 1000 THEN 'large'
    ELSE 0
  END AS size
FROM orders;
```

Лучше:

```sql
SELECT
  CASE
    WHEN amount > 1000 THEN 'large'
    ELSE 'small'
  END AS size
FROM orders;
```

Или:

```sql
SELECT
  CASE
    WHEN amount > 1000 THEN 1
    ELSE 0
  END AS is_large
FROM orders;
```

Все ветки должны возвращать совместимые значения.

### Не писать `ELSE` и удивляться `NULL`

Если `ELSE` нет и ни одно условие не подошло, результат будет `NULL`.

```sql
SELECT
  amount,
  CASE
    WHEN amount >= 1000 THEN 'large'
  END AS size
FROM orders;
```

Для заказа на 500 результатом будет `NULL`.

Обычно лучше добавить запасной вариант:

```sql
SELECT
  amount,
  CASE
    WHEN amount >= 1000 THEN 'large'
    ELSE 'small'
  END AS size
FROM orders;
```

### Сравнивать `NULL` через `=`

Неправильно:

```sql
SELECT
  CASE
    WHEN phone = NULL THEN 'no_phone'
    ELSE 'has_phone'
  END AS phone_status
FROM users;
```

Правильно:

```sql
SELECT
  CASE
    WHEN phone IS NULL THEN 'no_phone'
    ELSE 'has_phone'
  END AS phone_status
FROM users;
```

Для `NULL` нужны `IS NULL` и `IS NOT NULL`.

### Использовать `CASE`, когда достаточно обычного условия

Слишком сложно:

```sql
SELECT
  id,
  amount
FROM orders
WHERE
  CASE
    WHEN amount > 1000 THEN TRUE
    ELSE FALSE
  END;
```

Проще:

```sql
SELECT
  id,
  amount
FROM orders
WHERE amount > 1000;
```

`CASE` нужен для выбора одного результата из нескольких вариантов. Если условие одно и простое, обычный `WHERE` читается лучше.