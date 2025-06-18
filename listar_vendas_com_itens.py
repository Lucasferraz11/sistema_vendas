import mysql.connector

def listar_vendas():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
       password="Lucas2025@",
        database="sistema_vendas"
)
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT v.id, c.nome, v.data_venda, v.total
    FROM vendas v
    JOIN clientes c ON v.cliente_id = c.id
    """)
    vendas = cursor.fetchall()

    for venda in vendas:
        venda_id, nome_cliente, data_venda, total = venda
        print(f"\nVenda ID: {venda_id} - Cliente: {nome_cliente} - Data: {data_venda} - Total: {total:.2f}")
        print("Itens:")

        cursor.execute("""
        SELECT p.nome, iv.quantidade, p.preco
        FROM itens_venda iv
        JOIN produtos p ON iv.produto_id = p.id
        WHERE iv.venda_id = %s
        """, (venda_id,))
        itens = cursor.fetchall()

        for item in itens:
            nome_produto, quantidade, preco_unitario = item
            print(f" - Produto: {nome_produto} | Quantidade: {quantidade} | Preço Unitário: {preco_unitario:.2f}")

        cursor.close()
        conexao.close()
