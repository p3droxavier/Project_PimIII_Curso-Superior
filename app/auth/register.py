"""
  ' ln 24 ' - Retirar espaços e caracteres especias
  ' ln 24 ' - Adicionar verificação de quantidade e @#!345 etc na senha
"""


# Realiza o cadastro do usuário

import bcrypt
import json
import os
from app.utils.historico_utils import Historico

# Função para cadastrar um novo funcionario
def registerProfissional():
  try:
      nome = input("Digite o seu nome: ")
      email = input("Digite um email valido: ")
      
      # Chama a validação do email
      if not validarEmail(email):
        raise ValueError("Email invalido")
      
      document = input("Digite seu CPF. OBS, sem caracteres especiais: ")
      
      contato = int(input("Digite seu numero para contato:")) 
      cargo = input("Qual o seu cargo? ")
      especializacao = input("Qual a sua especialização? ")
      senha = input("Crie uma senha: ") # 

      confirmSenha = input("Confirme sua senha: ")
      
      # Chama a validação da senha e confirmar senha
      if not verificacaoDeSenha(senha, confirmSenha):
        raise ValueError("As senhas não coincidem")
      
      # Criptografa a senha
      hashPassword = senhaCriptografada(senha)
      
      # Dicionario com os dados do profissional. Contendo chave e valor.
      new_user =  {
        "nome": nome,
        "email": email,
        "document": document,
        "contato": contato,
        "cargo": cargo,
        "especializacao": especializacao,
        "senha": hashPassword,
        "isLogged":0 # Verifica se alguem  esta logado
      }
      
      # Realiza o cadastro do profissional
      caminho = 'app/data/users.json'
      
      # Verifica a exixtencia e o tamanho do arquivo
      if not os.path.exists(caminho) or os.path.getsize(caminho) == 0:
        users = []
        
      # Abrindo arquivo para leitura 
      else: 
        with open(caminho, "r", encoding="utf-8") as file:
          conteudo = file.read().strip() # le o conteudo do arquivo como string, remove espaços em branco 
          
          # Depois do strip o conteudo for uma string vazia "", não ha dados validos
          if not conteudo:
            users = []
            
          else: 
            users = json.loads(conteudo)
            # Garante que users seja uma lista 
            if not isinstance(users, list):
              users = []
              
      users.append(new_user)
      
      with open(caminho, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=2, ensure_ascii=False)
        
        
      # Fazendo o salvamento do histórico
      historico_paciente = "app/data/historico_user/historico_user.json"
      historico = Historico(arquivo=historico_paciente)
      historico.registrar(acao="Cadastro de usuário", usuario=new_user["nome"])
        
      
      # Chama a função de gerar a UI da dashboard
      # from app.auth.menu.menu import menu
      from app.main import home
      home()
      

        
  except ValueError as e:
    print("Erro")
    return

  
  
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
  
