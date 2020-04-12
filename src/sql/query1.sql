SELECT  T2.seller_id AS vendedor,
        SUM(T2.price) AS receita_total,
        COUNT( DISTINCT T1.order_id ) AS qtde_pedidos,
        COUNT( T2.product_id ) AS qtde_produtos

FROM tb_orders as T1

LEFT JOIN tb_order_items AS T2
ON T1.ORDER_ID = T2.ORDER_ID
WHERE T1.order_approved_at between '2017-06-01' AND '2018-06-01';
