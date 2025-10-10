import json
import os
from app.utils.historico_utils import Historico


# Pegando o nome do profissional
def getNameProfissional():
  caminho = 'app/data/users.json'
  
  if os.path.exists(caminho):
    with open(caminho, 'r') as file:
      users = json.load(file)
      for user in users:
        if user.get("isLogged") == 1:
          return user
  return None

def cadastrar_paciente():
    print("\n--- CADASTRO DE PACIENTES ---")
    nome = input("Nome: ")
    cpf = input("CPF: ") 
    email = input("E-mail ")
    # pacientes = {"nome": nome, "cpf": cpf, "E-mail": email}


    novo_paciente = {
        "nome": nome,
        "cpf": cpf,
        "email": email
    }


    caminho = 'app/data/pacientes/pacientes.json'
    
    if not os.path.exists(caminho) or os.path.getsize(caminho) == 0:
      users = []
      
    else:
      with open(caminho, "r", encoding="utf-8") as file:
        conteudo = file.read().strip()
        
        if not conteudo:
          users = []
          
        else:
          users = json.loads(conteudo)
          if not isinstance(users, list):
            users = []
            
    users.append(novo_paciente)
    
    with open(caminho, "w", encoding="utf-8") as file:
      json.dump(users, file, indent=2, ensure_ascii=False)
      
    
    # Salvando a ação no histórico
    user = getNameProfissional()
    historico_paciente = "app/data/historico_paciente/historico_paciente.json"
    historico = Historico(arquivo=historico_paciente)
    historico.registrarHistoricoPaciente(
      acao="Cadastro de pasciente",         # pega a ação
      paciente=novo_paciente["nome"],       # Pega o nome do paciente
      email=novo_paciente["email"],         # Pega o email do profissonal
      profissional=user['nome'],            #  Pega o nome do profissional
      especializacao_prof=user['especializacao']
    )
      
      



            