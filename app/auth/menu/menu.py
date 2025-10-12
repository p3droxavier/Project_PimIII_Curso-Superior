# Aqui ficara o menu de opções do sistema 
from app.auth.menu.register_paciente import cadastrar_paciente
from app.auth.menu.clinico.menu import estudos_clinicos
from app.auth.menu.farmaceuticos.gerenciar_estudos import gerenciar_estudos
from app.auth.menu.clinico.exames import gerar_relatorio_ambiental
from app.auth.login import signOut
import json
import os

# Verifica se tem algum usuário logado
def getLoggedProfissional():
  caminho = 'app/data/users.json'
  
  if os.path.exists(caminho):   # se o arquivo existir, ira abri-lo
    with open(caminho, 'r') as file: # # abre o arquivo no formato read 'r'
      users = json.load(file) # Guarda os dados do usuário na variavel
      for user in users: # Loop para mostrar todos os usuários
        if user.get("isLogged") == 1: # Dentre os usuários ira pegar apenas o que tem 'isLogged = 1'
          return user # retorna esse usuário
  return None # Se o arquivo estiver corrompido, ou nenhum usuário logado, retornará none


def menu():
  # Interface UI do Sistema
  while True:
    # Guarda os dados do usuário logado
    user = getLoggedProfissional()
    # Retorna o nome do usuário junto das boas vindas
    print(f"\nBem vindo ao sistema, {user['nome']}!")
    print("Digite: \n1 - Cadastrar um novo pasciente\n2 - Gerenciar estudos clinícos\n3 - Gerenciar estudos farmacêutico\n4 - Gerar relarorio ambiental\n5 - Deslogar")
    
    opcao = input("-> ")
    # Cadastrar um novo paciente
    if opcao == "1":
      cadastrar_paciente()
    # Navegar na sessão de Gerenciar estudos clinícos 
    elif opcao == "2":
      estudos_clinicos()
    # Navega na sessão de Gerenciar estudos farmacêutico
    elif opcao == "3":
      gerenciar_estudos()
    # Se a opção for igual a 4, interrompe o fluxo do loop e saira dessa UI
    elif opcao == "4":
      gerar_relatorio_ambiental() # Gera o relatorio ambiental
    elif opcao == "5":
      signOut() # Chama a função signout para deslogar o usuáriio
      break
    else:
      # Se a opção excolhia não for de 1 a 4, retornara essa mensagem
      print("\nOpção invalida! Tente novamente")
      

    
    
