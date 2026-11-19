
## INNER JOIN и связи многие-ко-многим

Иногда между сущностями связь многие-ко-многим.

Например:

- один студент может ходить на много курсов;
- один курс может иметь много студентов.

Для такой связи обычно делают промежуточную таблицу.

Таблица `students`:

|id|name|
|--:|---|
|1|Anna|
|2|Boris|

Таблица `courses`:

|id|title|
|--:|---|
|10|SQL Basics|
|20|Python Basics|

Таблица `student_courses`:

| student_id | course_id |
| ---------: | --------: |
|          1 |        10 |
|          1 |        20 |
|          2 |        10 |

Нужно получить список: студент — курс.

```sql
SELECT
  s.name AS student,
  c.title AS course
FROM students s
JOIN student_courses sc
  ON sc.student_id = s.id
JOIN courses c
  ON c.id = sc.course_id
ORDER BY s.name, c.title;
```

Результат:

|student|course|
|---|---|
|Anna|Python Basics|
|Anna|SQL Basics|
|Boris|SQL Basics|

Здесь `student_courses` — таблица-связка. Она помогает соединить студентов и курсы.

---
