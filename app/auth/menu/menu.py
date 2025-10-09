# Aqui ficara o menu de opções do sistema 
# Caminho - app/auth/menu/menu.py
# from ..login import login
from app.auth.menu.register_paciente import cadastrar_paciente
from app.auth.login import signOut
import json
import os

# Verifica se tem algum usuário logado
def getLoggedProfissional():
  caminho = 'app/data/users.json'
  
  if os.path.exists(caminho):
    with open(caminho, 'r') as file:
      users = json.load(file)
      for user in users:
        if user.get("isLogged") == 1:
          return user
  return None


def menu():
  
  while True:
    user = getLoggedProfissional()
    # if not user:
    #   print("\n Ainda não esta logado?? Faça o seu login agora!")
    #   login()
    #   continue
    
    print(f"\nBem vindo ao sistema, {user['nome']}!")
    print("Digite: \n1 - Cadastrar um novo pasciente\n2 - Cadastrar um novo exame\n3 - Listar todos os pascientes\n4 - Deslogar")
    
    opcao = input("-> ")
    
    if opcao == "1":
      cadastrar_paciente()
    elif opcao == "2":
      print("\nCadastrar um novo exame")
    elif opcao == "3":
      print("\nListar todos os pascientes")
    elif opcao == "4":
      signOut()
      break
    else:
      print("\nOpção invalida! Tente novamente")
      
      
if __name__ == '__main__':
  menu()
    
    
