# Realiza o login do funcionário

import os
import json
import bcrypt

# Função para fazer o login do funcionário
def login():
  nome = input("Digite o seu nome: ")
  email = input("Digite um email valido: ")
  document = input("Digite seu CPF.")
  cargo = input("Qual o seu cargo? ")
  especializacao = input("Qual a sua especialização? ")
  senha = input("Crie uma senha: ")
  
  
  if os.path.exists('./data/users.json'):
    with open('./data/users.json', 'r') as file:
      users = json.load(file)
      
    for user in users:
      if (user['nome'] == nome and 
          user['email'] == email and 
          user['document'] == document and 
          user['cargo'] == cargo and 
          user['especializacao'] == especializacao):
        
        if bcrypt.checkpw(senha.encode('utf-8'), user['senha'].encode('utf-8')):
          user['isLogged'] = 1
          with open('./data/users.json', 'w') as file:
            json.dump(users, file, indent=4)
        else:
          return print('Senha incorreta! ')
        break
        
      return print('Dados Invalidos! ')
  else: 
    return print('Não foi possivel encontrar o arquivo de usuário! ')
  
  
  
# Função para deslogar o profissional 
def signOut():
  if os.path.exists('./data/users.json'):
    with open('./data/users.json', 'r') as file:
      users = json.load(file)
      
      for user in users:
        if user['isLogged'] == 1:
          
          user['isLogged'] = 0
          with open('./data/users.json', 'w') as file:
            json.dump(users, file, indent=4)
            return print('Você saiu do sistema! ')