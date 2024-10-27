import os
from view import display_subtitle

def stock_menu():
    
    while True:
        display_subtitle("Módulo de Estoque")
        
        action = input("""
[1] Ver lista de produtos
[2] Cadastrar produto
[3] Atualizar cadastro de produto 
[4] Descontinuar produto
[5] Voltar ao menu principal""")
        break