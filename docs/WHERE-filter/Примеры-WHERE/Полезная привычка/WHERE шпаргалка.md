
## Короткая шпаргалка

|Задача|Пример|
|---|---|
|Равно|`WHERE status = 'paid'`|
|Не равно|`WHERE status <> 'cancelled'`|
|Больше|`WHERE amount > 1000`|
|Меньше или равно|`WHERE age <= 18`|
|Несколько условий сразу|`WHERE country = 'Russia' AND age >= 21`|
|Хотя бы одно условие|`WHERE status = 'paid' OR status = 'shipped'`|
|Значение в списке|`WHERE country IN ('Russia', 'Belarus')`|
|Значение не в списке|`WHERE status NOT IN ('cancelled', 'failed')`|
|Диапазон включительно|`WHERE price BETWEEN 100 AND 500`|
|Поиск по шаблону|`WHERE email LIKE '%@gmail.com'`|
|Значение отсутствует|`WHERE deleted_at IS NULL`|
|Значение есть|`WHERE deleted_at IS NOT NULL`|
