import pandas as pd
import mysql.connector
from mysql.connector import Error
import json

# Aqui temos uma função que cria a conexão com o mysql
def connect_to_db():
    
    with open('C:/Users/Felippe/OneDrive/Desktop/Projetos/Projeto ETL/config.json') as config_file:
        config = json.load(config_file)
    
    try:
        connection = mysql.connector.connect(
            host=config['db_host'],
            user=config['db_user'],
            password=config['db_password'],
            database=config['db_name']
        )
        
        if connection.is_connected():
            print("Conexão bem-sucedida com o MySQL")
        return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Essa faz a inserção de dados no banco de dados especificado no config.json
def insert_data_to_db(file_path, connection):
    
    df = pd.read_csv(file_path)


    cursor = connection.cursor()
    try:
        for index, row in df.iterrows():
            query = """
                INSERT INTO Compras_Shopping (Id,
                    Idade,Genero, Item_Comprado,
                    Valor_Comprado,Forma_Pagamento,
                    Compras_Anteriores,Frequencia_Compras
                ) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, tuple(row))
        connection.commit()
        print("Dados inseridos com sucesso!")
    except Error as e:
        print(f"Erro ao inserir dados: {e}")
        connection.rollback()
    finally:
        cursor.close()

# Encerra conexão com o bd.
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexão encerrada com sucesso.")


if __name__ == "__main__":

    file_path = 'C:/Users/Felippe/OneDrive/Desktop/Projetos/Projeto ETL/Data/AnaliseShopping_db.csv'


   
    connection = connect_to_db()

    if connection:
 
        insert_data_to_db(file_path, connection)

       
        close_connection(connection)
