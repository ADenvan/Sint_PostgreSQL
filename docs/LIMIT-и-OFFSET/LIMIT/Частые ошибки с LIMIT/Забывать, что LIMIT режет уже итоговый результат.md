
### Забывать, что LIMIT режет уже итоговый результат

Например:

```sql
SELECT customer_id, SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id
ORDER BY total_amount DESC
LIMIT 5;
```

`LIMIT` здесь берёт 5 клиентов уже после группировки и сортировки, а не 5 исходных заказов.

Это хорошо, если нужен топ клиентов. Но важно понимать, на каком этапе ты ограничиваешь данные.