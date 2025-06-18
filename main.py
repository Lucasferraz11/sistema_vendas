from clientes import cadastrar_cliente, excluir_cliente, atualizar_cliente
from produtos import cadastrar_produto, excluir_produto, atualizar_produto
from vendas import registrar_venda, excluir_venda, atualizar_venda
from listar_vendas_com_itens import listar_vendas
from exportar_vendas import exportar_vendas_para_csv

def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Produto")
        print("3 - Registrar Venda")
        print("4 - Listar Vendas com Itens")
        print("5 - Excluir Cliente")
        print("6 - Excluir Produto")
        print("7 - Excluir Venda")
        print("8 - Atualizar Cliente")
        print("9 - Atualizar Produto")
        print("10 - Atualizar Venda")
        print("11 - Exportar Vendas para CSV")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            cadastrar_cliente(nome, email)

        elif opcao == "2":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            cadastrar_produto(nome, preco)
        
        elif opcao == "3":
            cliente_id = int(input("ID do cliente: "))
            itens = []
            while True:
                produto_id = int(input("ID do produto: "))
                quantidade = int(input("Quantidade: "))
                itens.append((produto_id, quantidade))
                continuar = input("Adicionar outro produto? (s/n): ")
                if continuar.lower() != 's':
                    break
            registrar_venda(cliente_id, itens)
        
        elif opcao == "4":
            listar_vendas()
        
        elif opcao == "5":
            cliente_id = int(input("ID do cliente a excluir: "))
            excluir_cliente(cliente_id)
        
        elif opcao == "6":
            produto_id = int(input("ID do produto a excluir: "))
            excluir_produto(produto_id)
        
        elif opcao == "7":
            venda_id = int(input("ID da venda a excluir: "))
            excluir_venda(venda_id)
        
        elif opcao == "8":
            cliente_id = int(input("ID do cliente: "))
            nome = input("Novo nome do cliente: ")
            email = input("Novo email do cliente: ")
            atualizar_cliente(cliente_id, nome, email)
        
        elif opcao == "9":
            produto_id = int(input("ID do produto: "))
            nome = input("Novo nome do produto: ")
            preco = float(input("Novo preço do produto: "))
            atualizar_produto(produto_id, nome, preco)

        elif opcao == "10":
            venda_id = int(input("ID da venda: "))
            novos_itens = []
            while True:
                produto_id = int(input("ID do novo produto: "))
                quantidade = int(input("Quantidade: "))
                novos_itens.append((produto_id, quantidade))
                continuar = input("Adicionar outro produto? (s/n): ")
                if continuar.lower() != 's':
                    break
            atualizar_venda(venda_id, novos_itens)  

        elif opcao == "11":
             exportar_vendas_para_csv()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
