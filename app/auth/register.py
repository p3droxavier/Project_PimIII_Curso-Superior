# Realiza o cadastro do usuário

import bcrypt
import json
import os

# Função para cadastrar um novo funcionario
def registerProfissional():
  nome = input("Digite o seu nome: ")
  email = input("Digite um email valido: ")
  document = input("Digite seu CPF. OBS, sem caracteres especiais: ")
  contato = int(input("Digite seu numero para contato:")) # Retirar espaços e caracteres especias
  cargo = input("Qual o seu cargo? ")
  especializacao = input("Qual a sua especialização? ")
  senha = input("Crie uma senha: ") # Adicionar verificação de quantidade e @#!345 etc na senha
  confirmSenha = input("Confirme sua senha: ")
  
  
  # ============ Chamada as Validações ============
  
  if not validarEmail(email):
    return None
  
  if not verificacaoDeSenha(senha, confirmSenha):
    return None
  
  hashPassword = senhaCriptografada(senha)
  
  # ================================================


  # Dicionario com os dados do profissional. Contendo chave e valor.
  return {
    "nome": nome,
    "email": email,
    "document": document,
    "contato": contato,
    "cargo": cargo,
    "especializacao": especializacao,
    "senha": hashPassword,
    #"confirmsenha": confirmsenha,
    "isLogged":0 # Verifica se alguems esta logado
  }
  
  
  # ============ Validações ============
  # Validando email
def validarEmail(email):
  if "@" in email and "." in email and "com" in email:
    return True
  print("Email Invalido! ")
  return False 

# Verificação de senha && # Adicionar verificação de quantidade e @#!345 etc na senha
def verificacaoDeSenha(senha, confirmSenha):
  if senha != confirmSenha:
    print("As senhas não coincidem! ")
    return False
  return True

# Criptografia da senha
def senhaCriptografada(senha):
  senha_bytes = senha.encode('utf-8')
  salt = bcrypt.gensalt()
  hash_senha = bcrypt.hashpw(senha_bytes, salt)
  return hash_senha.decode('utf-8')

# ================================================
  
