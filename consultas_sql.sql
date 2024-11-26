select produto, categoria,preco, Quantidade, total_vendido from data_clean group by produto order by total_vendido desc;


select produto, total_vendido from data_clean where year(data) = 2024 and month(data) = 6  group by produto order by total_vendido asc limit 5;






