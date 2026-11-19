
## Как читать CREATE TABLE глазами разработчика

Когда видите `CREATE TABLE`, не пытайтесь читать его как набор случайных слов.

Читайте по смыслу:
```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(id),
  amount NUMERIC(12, 2) NOT NULL CHECK (amount > 0),
  status TEXT NOT NULL DEFAULT 'pending',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```
Это можно перевести так:

> Создаём таблицу заказов.  
> У каждого заказа есть уникальный `id`.  
> Каждый заказ принадлежит существующему пользователю.  
> Сумма заказа обязательна и должна быть больше нуля.  
> Статус обязателен, по умолчанию `pending`.  
> Дата создания обязательна, по умолчанию текущий момент.

Вот это и есть хорошее понимание SQL: вы видите не просто синтаксис, а правила предметной области.