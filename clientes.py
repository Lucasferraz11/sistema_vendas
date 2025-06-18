from conexao import conectar

def cadastrar_cliente(nome,email):
    if not nome.strip():
        print("O nome não pode estar vazio.")
        return
    if not email.strip():
        print("O email não pode estar vazio.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO clientes (nome,email) VALUES (%s, %s)"
    valores = (nome, email)


    cursor.execute(sql, valores)
    conexao.commit()

    print("Cliente cadastrado com sucesso!")
    cursor.close()
    conexao.close()

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")
    resultados = cursor.fetchall()

    print("Lista de Clientes:")
    for cliente in resultados:
        print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}")

    cursor.close()
    conexao.close()

def excluir_cliente(cliente_id):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
        conexao.commit()
        print(f"Cliente com ID {cliente_id} excluído com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir cliente: {e}")
    finally:    
        cursor.close()
        conexao.close()

def atualizar_cliente(cliente_id, nome, email):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "UPDATE clientes SET nome = %s, email = %s WHERE id = %s"
    cursor.execute(sql, (nome, email, cliente_id))
    conexao.commit()
    print("Cliente atualizado com sucesso!")
    cursor.close()
    conexao.close()

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes")
    for (id, nome, email) in cursor.fetchall():
        print(f"ID: {id}, Nome: {nome}, Email: {email}")
    cursor.close()

def buscar_cliente_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes WHERE nome LIKE %s", (f"%{nome}%",))
    resultados = cursor.fetchall()
    cursor.close()
    return resultados
