from conexao import conectar

try:
    conexao = conectar()
    print("Conexão bem-sucedida!")
    conexao.close()
except Exception as e:
    print(f"Erro ao conectar : {e}")