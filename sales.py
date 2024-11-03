from datetime import datetime
from database import load_data, write_data
from view import display_subtitle, clear_terminal

def validate_date_format(date_str):
    """Verifica se a data está no formato DD/MM/AAAA."""
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def display_sales_list():
    """Exibe a lista de vendas com detalhes formatados."""
    clear_terminal()
    display_subtitle("Tabela de vendas")
    
    sales_data = load_data("sales")  # Carrega os dados de vendas
    for sale in sales_data:
        print(f"Código: {sale['id']} | Nome: {sale['name']} | Valor da venda: {sale['sale_value']} | Data da venda: {sale['sale_date']}")
        
    input("\nDigite qualquer tecla para voltar para o módulo de vendas")
    sales_menu()  # Chama o menu de vendas

def create_product():
    """Cria um novo registro de venda."""
    clear_terminal()
    display_subtitle("Cadastro de vendas")
    
    sales_data = load_data("sales")
    name = input("Digite o nome da venda: ")
    value_sales = input("Digite o valor da venda: ")
    
    while True:
        entry_date = input("Forneça a data de entrada da venda (DD/MM/AAAA): ")
        if validate_date_format(entry_date):
            break
        print("Data inválida! Por favor, insira no formato DD/MM/AAAA.")
    
    current_id = sales_data[-1]["id"] + 1 if sales_data else 1
    
    sales_data.append({"id": current_id, "name": name, "value_sales": value_sales, "entry_date": entry_date})
    write_data("sales", sales_data)
    
    input("Digite qualquer tecla para voltar para o módulo de vendas")
    sales_menu()

def update_sale():
    """Atualiza um registro de venda existente."""
    clear_terminal()
    display_subtitle("Atualização de vendas")
    
    sales_data = load_data("sales")
    id = int(input("Digite o código da venda que deseja atualizar: "))
    
    for sale in sales_data:
        if sale['id'] == id:
            sale['name'] = input(f"Digite o novo nome da venda (atual: {sale['name']}): ") or sale['name']
            sale['value_sales'] = input(f"Digite o novo valor da venda (atual: {sale['value_sales']}): ") or sale['value_sales']
            
            while True:
                entry_date = input(f"Digite a nova data de entrada (atual: {sale['entry_date']}) [DD/MM/AAAA]: ") or sale['entry_date']
                if validate_date_format(entry_date):
                    sale['entry_date'] = entry_date
                    break
                print("Data inválida! Por favor, insira no formato DD/MM/AAAA.")
            break
    else:
        print("Venda não encontrada!")
    
    write_data("sales", sales_data)
    input("Digite qualquer tecla para voltar para o módulo de vendas")
    sales_menu()

def remove_sale():
    """Remove um registro de venda."""
    clear_terminal()
    display_subtitle("Exclusão de vendas")
    
    id = int(input("Digite o código da venda que deseja excluir: "))
    sales_data = load_data("sales")
    
    sales_data = [sale for sale in sales_data if sale['id'] != id]
    
    write_data("sales", sales_data)
    input("Digite qualquer tecla para voltar para o módulo de vendas")
    sales_menu()

def sales_menu():
    """Exibe o menu de opções do módulo de vendas."""
    action_list = {
        "1": display_sales_list,
        "2": create_product,
        "3": update_sale,
        "4": remove_sale
    }
    
    while True:
        clear_terminal()
        display_subtitle("Módulo de vendas")
        
        action = input("""
[1] Ver lista de vendas
[2] Cadastrar venda
[3] Atualizar cadastro de venda
[4] Excluir venda
[5] Voltar ao menu principal
Escolha uma opção: """)
        
        if action in action_list:
            action_list[action]()
            break
        elif action == "5":
            clear_terminal()
            break
        else:
            clear_terminal()
            print("A ação escolhida é inválida!")
