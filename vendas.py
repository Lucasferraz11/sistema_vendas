from conexao import conectar
from datetime import datetime

def registrar_venda(cliente_id, itens):
    conexao = conectar()
    cursor = conexao.cursor()

    total = 0
    for produto_id, quantidade in itens:
        cursor.execute("SELECT preco FROM produtos WHERE id = %s", (produto_id,))
        preco = cursor.fetchone()[0]
        total += preco * quantidade
        
    data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql_venda = "INSERT INTO vendas (cliente_id, data_venda, total) VALUES (%s, %s, %s)"
    cursor.execute(sql_venda, (cliente_id, data_venda, total))
    venda_id = cursor.lastrowid

    for produto_id, quantidade in itens:
        cursor.execute(
            "INSERT INTO itens_venda (venda_id, produto_id, quantidade) VALUES (%s, %s, %s)",
            (venda_id, produto_id, quantidade)
        )

    conexao.commit()
    print("Venda registrada com sucesso!")

    cursor.close()
    conexao.close()

def listar_vendas():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT v.id, c.nome, v.data_venda, v.total
        FROM vendas v
        JOIN clientes c ON v.cliente_id = c.id
    """
    cursor.execute(sql)
    vendas = cursor.fetchall()

    print("Lista de Vendas:")
    for venda in vendas:
        print(f"ID: {venda[0]}, Cliente: {venda[1]}, Data: {venda[2]}, Total: {venda[3]}")

    cursor.close()
    conexao.close()

def excluir_venda(venda_id):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM itens_venda WHERE venda_id = %s", (venda_id,))
        cursor.execute("DELETE FROM vendas WHERE id = %s", (venda_id,))
        conexao.commit()
        print(f"Venda ID {venda_id} e seus itens foram excluídos com sucesso!")
    except Exception as e:
        print("Erro ao excluir venda:", e)
    finally:
        cursor.close()
        conexao.close()

def atualizar_venda(venda_id, novos_itens):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM itens_venda WHERE venda_id = %s", (venda_id,))

    total = 0
    for produto_id, quantidade in novos_itens:
        cursor.execute("SELECT preco FROM produtos WHERE id = %s", (produto_id,))
        preco = cursor.fetchone()[0]
        total += preco * quantidade
        cursor.execute(
            "INSERT INTO itens_venda (venda_id, produto_id, quantidade) VALUES (%s, %s, %s)",
            (venda_id, produto_id, quantidade)
        )

    cursor.execute("UPDATE vendas SET total = %s WHERE id = %s", (total, venda_id))

    conexao.commit()
    print("Venda atualizada com sucesso!")
    cursor.close()
    conexao.close()
