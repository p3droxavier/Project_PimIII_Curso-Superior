# Realiza o login do funcionário

import os
import json
import bcrypt

# Função para fazer o login do funcionário
def login():
  nome = input("Digite o seu nome: ")
  email = input("Digite um email valido: ")
  document = input("Digite seu CPF: ")
  cargo = input("Qual o seu cargo? ")
  especializacao = input("Qual a sua especialização? ")
  senha = input("Coloque sua senha: ")
  
  caminho = './data/users.json'
  
  # Verifica se a pasta existe
  if not os.path.exists(caminho):
    print('Não foi possivel encontrar o arquivo')
    return
  
  # Carrega os usuário 
  with open(caminho, 'r') as file:
    users = json.load(file)
    
  usuario_encontrado = False
    
  for user in users:
    #Verificação de nome, email, document, cargo, especialização e senha
    if (user['nome'] == nome and 
        user['email'] == email and 
        user['document'] == document and 
        user['cargo'] == cargo and 
        user['especializacao'] == especializacao):
      
        usuario_encontrado = True
      
        if bcrypt.checkpw(senha.encode('utf-8'), user['senha'].encode('utf-8')):
          # Desloga todos os outros usuários antes
          for u in users:
            u['isLogged'] = 0
            
          user['isLogged'] = 1 # Marca este como logado
          
          with open(caminho, 'w') as file:
            json.dump(users, file, indent=4)
            
          print('\nLogin bem sucedido!')
          return
        
        else: 
          print('Senha incorreta! Certifique-se de que escreveu a senha correta')
          return
  
  if not usuario_encontrado:
    print('Dados Invalidos! Nenhum usuário encontrado com essas informações!')

  
  
  
# Função para deslogar o profissional 
def signOut():
  
  caminho = './data/users.json'
  
  if os.path.exists(caminho):
    with open(caminho, 'r') as file:
      users = json.load(file)
      
      for user in users:
        if user['isLogged'] == 1:
          
          user['isLogged'] = 0
          with open(caminho, 'w') as file:
            json.dump(users, file, indent=4)
            return print('Você saiu do sistema! ')