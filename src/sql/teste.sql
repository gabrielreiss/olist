SELECT seller_id,
FROM tb_orders

LEFT JOIN tb_sellers
ON tb_orders.seller_id = seller_id


WHERE order_delivered_customer_date 
BETWEEN '2017-01-01' AND '2017-12-31';