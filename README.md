# 🛒 Sistema de Cadastro e Vendas

Este repositório contém um sistema completo de gerenciamento de **clientes**, **produtos** e **vendas**, desenvolvido em **Python** com banco de dados **MySQL**, utilizado como parte dos meus estudos em automação, backend e manipulação de dados.

As funcionalidades incluem inserção, listagem, atualização, exclusão e exportação de dados. Toda a interface é baseada em terminal.

---

## 🎯 Objetivo do repositório

✅ Consolidar meu aprendizado em Python, SQL e automação de sistemas  
✅ Praticar integração com banco de dados MySQL  
✅ Criar um portfólio funcional com operações reais de CRUD  

---

## 📚 Funcionalidades

- Cadastro de clientes e produtos
- Registro de vendas com múltiplos itens
- Atualização e exclusão de registros
- Listagem de vendas com seus produtos detalhados
- Exportação de vendas para CSV
- Interface via menu no terminal

---

## 🧪 Tecnologias utilizadas

- Python 3.13+
- MySQL
- mysql-connector-python
- CSV (nativo do Python)

---

## 🗂 Estrutura do projeto

sistema_vendas/
├── clientes.py # Funções de clientes
├── produtos.py # Funções de produtos
├── vendas.py # Funções de vendas
├── listar_vendas_com_itens.py # Consulta detalhada de vendas
├── exportar_vendas.py # Geração de CSV
├── conexao.py # Conexão com MySQL
├── main.py # Menu principal
└── README.md


---

## ⚙️ Pré-requisitos

- Python 3 instalado
- MySQL instalado e rodando
- Instale a lib de conexão:

```bash
pip install mysql-connector-python
