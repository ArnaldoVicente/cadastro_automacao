import csv
import os

# Função para adicionar um novo cliente
def adicionar_cliente(nome, email, telefone):
    with open('clientes.csv', mode='a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, email, telefone])
    print("Cliente adicionado com sucesso!")

# Função para visualizar todos os clientes cadastrados
def visualizar_clientes():
    with open('clientes.csv', mode='r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(f"Nome: {linha[0]}, Email: {linha[1]}, Telefone: {linha[2]}")

# Função para buscar um cliente pelo nome
def buscar_cliente_por_nome(nome):
    with open('clientes.csv', mode='r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha[0].lower() == nome.lower():
                print(f"Nome: {linha[0]}, Email: {linha[1]}, Telefone: {linha[2]}")
                return
        print("Cliente não encontrado.")

# Função principal
def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar cliente")
        print("2. Visualizar todos os clientes")
        print("3. Buscar cliente por nome")
        print("4. Encerrar o programa")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            adicionar_cliente(nome, email, telefone)
        elif escolha == '2':
            visualizar_clientes()
        elif escolha == '3':
            nome = input("Digite o nome do cliente que deseja buscar: ")
            buscar_cliente_por_nome(nome)
        elif escolha == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
