
## Условия в WHERE могут быть сложными

В `WHERE` можно писать не только `id = 1`.

Можно использовать те же условия, что и в обычном `SELECT`:
```sql
UPDATE users
SET promo_code = 'WELCOME10'
WHERE country = 'Russia' AND tier = 'free';
```
Этот запрос выдаст промокод всем пользователям из России на бесплатном тарифе.

Другой пример:
```sql
UPDATE orders
SET status = 'archived'
WHERE created_at < NOW() - INTERVAL '1 year';
```
Здесь мы архивируем старые заказы, созданные больше года назад.

Можно использовать:
- `AND`;
- `OR`;
- `NOT`;
- `IN`;
- `BETWEEN`;
- `LIKE`;
- сравнения `>`, `<`, `>=`, `<=`;
- проверки на `NULL`.

Например:
```sql
UPDATE users
SET email_confirmed = FALSE
WHERE email IS NULL;
```
`WHERE` — это фильтр. Чем точнее фильтр, тем безопаснее обновление.