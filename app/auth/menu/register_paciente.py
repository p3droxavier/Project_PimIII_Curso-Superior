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

    # O 'r' é de ler em ingles
    # as file, faz com que dos dados do arquivo apelidado de file
    arquivo = 'app/data/pacientes/pacientes.json'
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as file: 
            users = json.load(file)
            print("teste02")
        users.append(novo_paciente)
        # O 'w' é de write, escrever, ja que vc vai escrever um novo pasciente
        with open(arquivo, 'w') as file:
            json.dump(users, file, indent=4)
    else:
        with open(arquivo, 'w') as file:
            json.dump([novo_paciente], file, indent=4)



            