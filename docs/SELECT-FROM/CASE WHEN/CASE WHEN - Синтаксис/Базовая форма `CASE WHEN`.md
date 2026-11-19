
## Базовая форма `CASE WHEN`

Самая частая форма называется searched `CASE`.

Она выглядит так:

```sql
CASE
  WHEN condition_1 THEN result_1
  WHEN condition_2 THEN result_2
  WHEN condition_3 THEN result_3
  ELSE default_result
END
```

Читается почти как обычный текст:

- если выполнено первое условие — верни первый результат;
- иначе если выполнено второе условие — верни второй результат;
- иначе если выполнено третье условие — верни третий результат;
- если ничего не подошло — верни значение из `ELSE`.

Например:

```sql
SELECT
  student_name,
  score,
  CASE
    WHEN score >= 90 THEN 'excellent'
    WHEN score >= 70 THEN 'good'
    WHEN score >= 50 THEN 'ok'
    ELSE 'failed'
  END AS result
FROM exams;
```

Если у студента `score = 82`, результат будет `good`.

Если `score = 45`, результат будет `failed`.