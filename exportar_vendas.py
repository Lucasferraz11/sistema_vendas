import csv
from conexao import conectar

def exportar_vendas_para_csv(nome_arquivo="relatorio_vendas.csv"):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        SELECT v.id, c.nome AS cliente, v.data_venda, p.nome AS produto,
               iv.quantidade, p.preco, v.total
        FROM vendas v
        JOIN clientes c ON v.cliente_id = c.id
        JOIN itens_venda iv ON iv.venda_id = v.id
        JOIN produtos p ON iv.produto_id = p.id
        ORDER BY v.id;
    """
    
    cursor.execute(sql)
    resultados = cursor.fetchall()

    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(["Venda ID", "Cliente", "Data da Venda", "Produto", "Quantidade", "Preço Unitário", "Total da Venda"])

        for linha in resultados:
            escritor.writerow(linha)

    cursor.close()
    conexao.close()
    print(f"Relatório exportado com sucesso para '{nome_arquivo}'!")
