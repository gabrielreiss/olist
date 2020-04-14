SELECT *
FROM tb_orders
WHERE order_delivered_customer_date BETWEEN '{data_init}' AND '{data_end}';