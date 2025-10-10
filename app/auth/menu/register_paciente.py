import json
import os


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



            