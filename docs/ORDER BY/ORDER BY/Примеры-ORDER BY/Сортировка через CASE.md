
## Сортировка через CASE

Иногда обычная сортировка по алфавиту не подходит.

Например, есть статусы заказов:

- paid;
- pending;
- cancelled.

Если отсортировать по статусу как по строке, база расставит их по алфавиту. Но бизнесу может быть нужен другой порядок: сначала оплаченные, потом ожидающие, потом отменённые.

Для такого случая используют `CASE` в `ORDER BY`.

Допустим, есть таблица `orders`:

|id|customer|amount|status|created_at|
|--:|---|--:|---|---|
|1|Anna|500|paid|2024-03-10|
|2|Boris|1500|paid|2024-03-15|
|3|Vera|200|cancelled|2024-03-12|
|4|Gregory|3000|paid|2024-03-08|
|5|Denis|800|pending|2024-03-15|

Нужно вывести заказы так:

1. Сначала `paid`.
2. Потом `pending`.
3. Потом `cancelled`.
4. Внутри каждого статуса — новые заказы выше старых.
5. Если даты одинаковые — большая сумма выше.

Запрос:

```sql
SELECT id, customer, status, amount, created_at
FROM orders
ORDER BY
  CASE status
    WHEN 'paid' THEN 1
    WHEN 'pending' THEN 2
    WHEN 'cancelled' THEN 3
    ELSE 4
  END,
  created_at DESC,
  amount DESC;
```

Результат:

|id|customer|status|amount|created_at|
|--:|---|---|--:|---|
|2|Boris|paid|1500|2024-03-15|
|1|Anna|paid|500|2024-03-10|
|4|Gregory|paid|3000|2024-03-08|
|5|Denis|pending|800|2024-03-15|
|3|Vera|cancelled|200|2024-03-12|

`CASE` здесь превращает статусы в условные числа для сортировки:

- paid получает 1;
- pending получает 2;
- cancelled получает 3;
- всё остальное получает 4.

Так мы сортируем не по алфавиту, а по смыслу.