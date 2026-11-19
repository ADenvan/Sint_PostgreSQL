
## AND: когда должны выполниться все условия

`AND` означает «и».

Строка попадёт в результат только если **все условия** истинны.

Например:

```sql
SELECT id, name, country, age
FROM users
WHERE country = 'Russia' AND age >= 21;
```

Читается так:

> Верни пользователей, у которых страна `Russia` и возраст 21 или больше.

Есть таблица `users`.

|id|name|country|age|
|--:|---|---|--:|
|1|Anna|Russia|25|
|2|Bob|USA|30|
|3|Vera|Russia|17|
|4|Grigory|Russia|40|

Запрос:

```sql
SELECT name
FROM users
WHERE country = 'Russia' AND age >= 21;
```

Результат:

|name|
|---|
|Anna|
|Grigory|

Почему?

- `Anna` подходит: страна `Russia`, возраст `25`.
- `Bob` не подходит: возраст подходит, но страна `USA`.
- `Vera` не подходит: страна подходит, но возраст `17`.
- `Grigory` подходит: страна `Russia`, возраст `40`.

Для `AND` нужно, чтобы совпало всё.