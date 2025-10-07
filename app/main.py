# Aqui ficara a verificação se tem alguem logado
# Se estiver um usuário logado ira levar ele para a 1° camada do sistema

# Se não estiver, jogará para o Register(Cadastro) e depois Login() 

from auth.register import registerProfissional
from auth.login import login
import bcrypt
import json
import os

# Verifica se tem algum usuário logado
# def getLoggedProfissional():
#   if os.path.exists('data/users.json'):
#     with open('data/users.json') as file:
#       users = json.load(file)
#       for user in users:
#         if user.get("isLogged") == 1:
#           return user
#   return None



def home():
  while True:
    
    print("\nOlá, Bem Vindo")
    print("Digite: \n1 - Logar\n2 - Cadastrar\n3 Encerrar o programa")
    option = input("-> ")
    
    if option == "1":
      login()
      
    elif option == "2":
      dados = registerProfissional()
      
      if dados:
        if os.path.exists('./data/users.json'):
          with open('./data/users.json', 'r') as file:
            users = json.load(file)
          users.append(dados)
          with open('./data/users.json', 'w') as file:
            json.dump(users, file, indent=4)
            
        else:
          with open('./data/users.json', 'w') as file:
            json.dump([dados], file, indent=4)
            
    elif option == "3":
      print("Encerrando o programa")
      break
    
    else:
      print("Opção inválida! Tente novamente mais tarde.")
  
    

  
    
    






if __name__ == "__main__":
  home()
#   if getLoggedProfissional():
#     None
#   Se o usuário não estiver cadastrado chama essa função
#   dados = registerProfissional()
  
#   if dados:
#     if os.path.exists('./data/users.json'):
#       with open('./data/users.json', 'r') as file:
#         users = json.load(file)
#       users.append(dados)
#       with open('./data/users.json', 'w') as file:
#         json.dump(users, file, indent=4)
        
#     else:
#       with open('./data/users.json', 'w') as file:
#         json.dump([dados], file, indent=4)
  
# Se ele ainda não estiver cadastrado, chama o login