# Projeto de ETL: Análise de um Shopping Fictício

## Descrição do Projeto

Este projeto consiste em um pipeline de ETL (Extração, Transformação e Carga) desenvolvido para analisar dados de um shopping fictício. O objetivo é fornecer insights sobre o comportamento de compra dos clientes, utilizando técnicas de análise de dados e visualização.

---

## Estrutura do Projeto

### Diretórios

- **data/**: Contém o arquivo inicial `shopping_trends.csv` com os dados brutos.
- **Data Visualization/**: Contém o dashboard com a visualização de dados referente a operação de um shopping em um determinado mês.
- **notebooks/**: Contém notebooks Jupyter para exploração e análise de dados. Arquivo principal: `ETL_AnaliseShopping.ipynb`.
- **scripts/**: Scripts Python que implementam diferentes componentes do projeto:
  - **shopping_etl.py**: Realiza o pipeline de ETL completo.

### Arquivos

- **README.md**: Este arquivo, com a documentação do projeto.
- **config.json**: Armazena as credenciais para conexão com o banco de dados MySQL (ignorado pelo `.gitignore`).
- **Queries_Perguntas_de_negocio.sql**: Arquivo com as queries responsáveis pelas perguntas de negócio do case.

---

## Funcionalidades

### ETL (Extração, Transformação e Carga)

- Extração dos dados do arquivo CSV inicial.
- Limpeza e transformação dos dados para normalização e organização.
- Carga dos dados transformados no banco de dados MySQL.

### Consultas SQL

- Geração de insights com consultas otimizadas.
- Exemplo: Identificação dos produtos mais vendidos por faixa horária.

### Visualizações

- Dashboard criado com gráficos e cards no Power BI para representação clara dos resultados.
- Exemplos:
  - Gráfico de Receita por produto.

---

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - `pandas` e `numpy` para manipulação de dados.
  - `mysql.connector` para conexão e interação com o banco de dados.
- **Banco de Dados**: MySQL
- **Ambiente Virtual**: Gerenciado com `venv`.

---

