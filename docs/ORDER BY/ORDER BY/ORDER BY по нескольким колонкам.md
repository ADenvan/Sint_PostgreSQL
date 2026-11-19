
## ORDER BY по нескольким колонкам

Иногда одной колонки для сортировки недостаточно.

Например, мы хотим отсортировать сотрудников сначала по отделу, а внутри каждого отдела — по зарплате от большей к меньшей.

Для этого в `ORDER BY` можно перечислить несколько колонок через запятую:

```sql
SELECT name, department, salary
FROM employees
ORDER BY department ASC, salary DESC;
```

База будет сортировать так:

1. Сначала по `department ASC`.
2. Если отдел одинаковый — внутри отдела по `salary DESC`.
3. Если и зарплата одинаковая — порядок между такими строками всё ещё может быть произвольным.

Допустим, есть таблица `employees`:

|id|name|department|salary|
|--:|---|---|--:|
|1|Anna|IT|120000|
|2|Boris|Sales|80000|
|3|Vera|IT|150000|
|4|Gregory|HR|70000|
|5|Denis|IT|120000|
|6|Elena|Sales|95000|

Запрос:

```sql
SELECT name, department, salary
FROM employees
ORDER BY department ASC, salary DESC;
```

Результат:

|name|department|salary|
|---|---|--:|
|Gregory|HR|70000|
|Vera|IT|150000|
|Anna|IT|120000|
|Denis|IT|120000|
|Elena|Sales|95000|
|Boris|Sales|80000|

Сначала идут отделы по алфавиту: HR, IT, Sales. А внутри каждого отдела сотрудники отсортированы по зарплате от большей к меньшей.

Но обрати внимание: у Anna и Denis одинаковый отдел и одинаковая зарплата. Значит, между ними порядок не гарантирован. Сегодня Anna может быть выше Denis, завтра наоборот.

Если нужен стабильный и предсказуемый порядок, добавь ещё одну колонку:

```sql
SELECT name, department, salary
FROM employees
ORDER BY department ASC, salary DESC, name ASC;
```

Теперь при одинаковой зарплате сотрудники будут отсортированы по имени.