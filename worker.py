import os
import json
import re
from view import clear_terminal

file = os.path.join(os.path.dirname(__file__), "user.json")

def load_user():
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f, indent=4)
    with open(file, "r") as f:
        return json.load(f)

def format_cpf(cpf):
   #remove caracter especial
    return re.sub(r'\D', '', cpf)

def add_worker(name, age, cpf, job):
    workers = load_user()
    cpf = format_cpf(cpf)  # Formata o CPF digitado

    # Verifica se o CPF já existe 
    if any(format_cpf(worker['cpf']) == cpf for worker in workers):
        print("CPF já cadastrado! Tente novamente.")
        return
    
    # Adiciona o trabalhador ao JSON com CPF no formato padrão
    workers.append({"name": name, "age": age, "cpf": cpf, "job": job})
    with open(file, 'w') as f:
        json.dump(workers, f, indent=4, ensure_ascii=False)
    print("Registro concluído com sucesso!")

def list_workers():
    workers = load_user()
#lista trabalhador
    if workers:
        max_len = max(len(f"NOME: {worker['name']}, IDADE: {worker['age']}, CPF: {worker['cpf']}, CARGO: {worker['job']}") for worker in workers)
        print("=" * max_len)
        print("LISTA DE FUNCIONÁRIOS:")
        print("-" * max_len)
        for worker in workers:
            print("*" * max_len)
            print(f"NOME: {worker['name']}, IDADE: {worker['age']}, CPF: {worker['cpf']}, CARGO: {worker['job']}")
            print("*" * max_len)
        print("=" * max_len)
    else:
        print("Nenhum usuário registrado.")

def update_worker(old_name, new_name, new_age, new_cpf, new_job):
    workers = load_user()
#atualiza trabalhador
    updated = False
    for worker in workers:
        if worker['name'] == old_name:
            worker['name'] = new_name
            worker['age'] = new_age
            worker['cpf'] = format_cpf(new_cpf)  # Formata o CPF atualizado
            worker['job'] = new_job
            updated = True
            break
    if updated:
        with open(file, 'w') as f:
            json.dump(workers, f, indent=4, ensure_ascii=False)
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")

def remove_worker(name):
    workers = load_user()
#remove trabalhador
    new_workers = [worker for worker in workers if worker['name'] != name]
    if len(new_workers) != len(workers):
        with open(file, 'w') as f:
            json.dump(new_workers, f, indent=4, ensure_ascii=False)
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado.")

def find_worker(name):
    workers = load_user()
#busca trabalhador
    found = False
    for worker in workers:
        if worker['name'] == name:
            print(f"NOME: {worker['name']}, IDADE: {worker['age']}, CPF: {worker['cpf']}, CARGO: {worker['job']}")
            found = True
            break
    if not found:
        print("Usuário não encontrado.")

def show_menu():
    clear_terminal()
    while True:
        print("\nMENU:")
        print("1. ADICIONAR USUÁRIO")
        print("2. LISTAR USUÁRIOS")
        print("3. ATUALIZAR USUÁRIO")
        print("4. EXCLUIR USUÁRIO")
        print("5. BUSCAR UM USUÁRIO")
        print("6. SAIR")

        option = input("Escolha uma opção: ")

        if option == '1':
            clear_terminal()
            name = input("Nome: ")
            age = input("Idade: ")
            cpf = input("CPF (formato 000.000.000-00): ")
            job = input("Cargo: ")
            add_worker(name, age, cpf, job)
        elif option == '2':
            clear_terminal()
            list_workers()
        elif option == '3':
            clear_terminal()
            old_name = input("Nome do usuário para atualizar: ")
            new_name = input("Novo nome: ")
            new_age = input("Nova idade: ")
            new_cpf = input("Novo CPF (formato 000.000.000-00): ")
            new_job = input("Novo cargo: ")
            update_worker(old_name, new_name, new_age, new_cpf, new_job)
        elif option == '4':
            clear_terminal()
            name = input("Nome do usuário para excluir: ")
            remove_worker(name)
        elif option == '5':
            clear_terminal()
            name = input("Nome do usuário para buscar: ")
            find_worker(name)
        elif option == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

show_menu()




         