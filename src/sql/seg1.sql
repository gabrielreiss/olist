SELECT  T2.seller_id,
        SUM( T2.price ) AS receita_total, /* Calcula receita total por vendedor */
        COUNT( DISTINCT T1.order_id ) AS qtde_pedidos, /* conta pedidos unicos*/
        COUNT( T2.product_id ) AS qtde_produtos, /* conta quantidade de produtos */
        COUNT( DISTINCT T2.product_id ) AS qtde_produtos, /* conta quantidade de produtos diferentes */
        MIN( DATEDIFF( CAST('2018-06-01' AS DATE), 
					    CAST(T1.order_approved_at AS DATE) )  ) AS qtde_dias_ult_venda /* quantidade de dias da ultima venda */


FROM tb_orders AS T1 /* */

INNER JOIN tb_order_items as T2  /* Junta com a tabela de pedido de itens */
ON T2.order_id = T1.order_id    /* Define as variáveis que se juntam */

WHERE T1.order_approved_at              
BETWEEN '2017-06-01' AND '2018-06-01'   /* Define um corte no tempo */

GROUP BY T2.seller_id; /* Agrupa por vendedores */