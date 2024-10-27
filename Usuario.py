import os
import json
from datetime import datetime

arquivo = os.path.join(os.path.dirname(__file__), 'funcionarios.json')

def carregar_funcionarios():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)
    
    with open(arquivo, 'r') as f:
        return json.load(f)
def adicionar_funcionario():
    funcionarios = carregar_funcionarios()
    cpf = input("Digite o CPF do funcionário: ")

    if any(funcionario['cpf'] == cpf for funcionario in funcionarios):
        print("CPF já cadastrado! Tente novamente.")
        return

    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    data_contratacao = input("Digite a data de contratação (DD/MM/AAAA): ")
    
    try:
        datetime.strptime(data_contratacao, "%d/%m/%Y")
    except ValueError:
        print("Data de contratação inválida! Use o formato DD/MM/AAAA.")
        return
    
    try:
        salario = float(input("Digite o salário do funcionário: "))
    except ValueError:
        print("Salário inválido! Insira um número.")
        return

    novo_funcionario = {
        'cpf': cpf,
        'nome': nome,
        'cargo': cargo,
        'data_contratacao': data_contratacao,
        'salario': salario
    }
    funcionarios.append(novo_funcionario)

    with open(arquivo, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)
    print("Funcionário adicionado com sucesso.")

def listar_funcionarios():
    funcionarios = carregar_funcionarios()
    if funcionarios:
        print("\nLista de Funcionários:")
        print("-" * 50)
        for funcionario in funcionarios:
            print(f"CPF: {funcionario['cpf']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Data de Contratação: {funcionario['data_contratacao']}")
            print(f"Salário: R${funcionario['salario']:.2f}")
            print("-" * 50)
    else:
        print("Nenhum funcionário cadastrado.")

def atualizar_funcionario():
    cpf = input("Digite o CPF do funcionário que deseja atualizar: ")
    novo_nome = input("Novo nome (ou Enter para manter o atual): ")
    novo_cargo = input("Novo cargo (ou Enter para manter o atual): ")
    nova_data_contratacao = input("Nova data de contratação (DD/MM/AAAA) (ou Enter para manter): ")
    novo_salario = input("Novo salário (ou Enter para manter o atual): ")
    novo_salario = float(novo_salario) if novo_salario else None

    funcionarios = carregar_funcionarios()
    for funcionario in funcionarios:
        if funcionario['cpf'] == cpf:
            if novo_nome:
                funcionario['nome'] = novo_nome
            if novo_cargo:
                funcionario['cargo'] = novo_cargo
            if nova_data_contratacao:
                funcionario['data_contratacao'] = nova_data_contratacao
            if novo_salario:
                funcionario['salario'] = novo_salario
            break

    with open(arquivo, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)
    print("Funcionário atualizado com sucesso.")

def excluir_funcionario():
    cpf = input("Digite o CPF do funcionário que deseja excluir: ")
    funcionarios = carregar_funcionarios()
    funcionarios = [func for func in funcionarios if func['cpf'] != cpf]

    with open(arquivo, 'w') as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)
    print("Funcionário excluído com sucesso.")

def buscar_funcionario():
    cpf = input("Digite o CPF do funcionário que deseja buscar: ")
    funcionarios = carregar_funcionarios()
    encontrado = False
    for funcionario in funcionarios:
        if funcionario['cpf'] == cpf:
            print(f"CPF: {funcionario['cpf']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Data de Contratação: {funcionario['data_contratacao']}")
            print(f"Salário: R${funcionario['salario']:.2f}")
            encontrado = True
            break
    if not encontrado:
        print("Funcionário não encontrado.")

def menu():
    while True:
        print("\n==== MENU DE FUNCIONÁRIOS ====")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Excluir Funcionário")
        print("5. Buscar Funcionário")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_funcionario()
        elif opcao == '2':
            listar_funcionarios()
        elif opcao == '3':
            atualizar_funcionario()
        elif opcao == '4':
            excluir_funcionario()
        elif opcao == '5':
            buscar_funcionario()
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


menu()
