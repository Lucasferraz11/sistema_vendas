from conexao import conectar
def cadastrar_produto(nome, preco):
    if not nome.strip():
        print("O nome do produto não pode estar vazio.")
        return
    if preco <= 0:
        print("O preço do produto deve ser maior que zero.")
        return
    
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
    valores = (nome, preco)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Produto cadastrado com sucesso!")
    cursor.close()
    conexao.close()

def listar_produtos():  
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")
    resultados = cursor.fetchall()

    print("Lista de Produtos:")
    for produto in resultados:
        print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}")

    cursor.close()
    conexao.close()

def excluir_produto(produto_id):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM produtos WHERE id = %s", (produto_id,))
        conexao.commit()
        print(f"Produto ID {produto_id} excluído com sucesso!")
    except Exception as e:
        print("Erro ao excluir produto:", e)
    finally:
        cursor.close()
        conexao.close()

def atualizar_produto(produto_id, nome, preco):
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "UPDATE produtos SET nome = %s, preco = %s WHERE id = %s"
        cursor.execute(sql, (nome, preco, produto_id))
        conexao.commit()
        print("Produto atualizado com sucesso!")
        cursor.close()
        conexao.close()
    
def listar_produtos():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, preco FROM produtos")
        for (id, nome, preco) in cursor.fetchall():
            print(f"ID: {id}, Nome: {nome}, Preço: {preco:.2f}")
        cursor.close()

def buscar_produto_por_nome(nome):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, preco FROM produtos WHERE nome LIKE %s", (f"%{nome}%",))
        resultados = cursor.fetchall()
        cursor.close()
        return resultados


