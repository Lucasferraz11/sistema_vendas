import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Lucas2025@',
        database='sistema_vendas'
    )
    return conexao