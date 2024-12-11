-- Utilizando o banco de dados "shopping_db"
use shopping_db;

-- Visualização de todos os dados do banco de dados
select * from compras_shopping;

-- Proporção de compras entre os gêneros
SELECT 
    Genero,
    COUNT(*) AS Total_Compras,
    ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Compras_Shopping)), 2) AS Proporcao_Percentual
FROM Compras_Shopping
GROUP BY Genero;

-- Receita Total
SELECT 
    SUM(Valor_Comprado) AS Valor_Total_Comprado
FROM Compras_Shopping;

-- Quais as formas de pagamento mais utilizadas?
SELECT 
    Forma_Pagamento,
    COUNT(*) AS Total_Utilizacao
FROM Compras_Shopping
GROUP BY Forma_Pagamento
ORDER BY Total_Utilizacao DESC;

-- Quais os produtos que geraram mais receita para o shopping?
SELECT 
    Item_Comprado,
    SUM(Valor_Comprado) AS Receita_Total
FROM Compras_Shopping
GROUP BY Item_Comprado
ORDER BY Receita_Total DESC;

-- Qual foi o valor gasto por cliente por compra (ticket médio)?
SELECT 
    AVG(Valor_Comprado) AS Valor_Medio_Por_Compra
FROM Compras_Shopping;






