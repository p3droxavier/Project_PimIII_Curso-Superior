import json
import os
from app.utils.historico_utils import Historico
from app.auth.menu.clinico.arvore_paciente import Pacientes, ArvorePaciente

# Criando árvore para armazenar pacientes na execução
arvore = ArvorePaciente()
arvore.carregar_de_json()

def cadastrar_paciente():
    print("\n--- CADASTRO DE PACIENTES ---")
    
    """ Com base nos estudos disponíveis, o profissional irá adicionar o paciente a esse estudo """
    
    # === Carrega estudos disponíveis ===
    caminho_estudos = "app/data/estudos_clinicos/estudos_salvos.json"
    if not os.path.exists(caminho_estudos):
        print("\nNenhum estudo cadastrado ainda.")
        return
    
    with open(caminho_estudos, "r", encoding="utf-8") as file:
        try:
            estudos = json.load(file)
        except json.JSONDecodeError:
            print("Erro ao carregar arquivo")
            return
    
    if not estudos:
        print("\nNenhum estudo cadastrado ainda.")
        return
    
    # === Exibe estudos para o usuário escolher ===
    print("\nEstudos disponíveis: ")
    for i, est in enumerate(estudos, 1):
        print(f"{i} - {est['nome']}")  # Não mostramos mais fase
    
    try:
        escolha = int(input("Selecione um estudo para o paciente: "))
        if escolha < 1 or escolha > len(estudos):
            print("\nEscolha inválida")
            return
    except ValueError:
        print("Opção inválida")
        return
    
    estudo_escolhido = {
        "nome": estudos[escolha - 1]["nome"]
    }
    
    # === Coleta dos dados ===
    nome = input("Nome: ")
    idade = int(input("Idade do paciente: "))
    sexo = input("Sexo do paciente: ").strip().upper()[0]  # Pega a 1ª letra maiúscula
    cpf = input("CPF do paciente: ")
    if not validarCpf(cpf):
        print("\nCPF inválido")
        return
    email = input("E-mail do paciente: ")
    if not validarEmail(email):
        return
    
    # === Cria o objeto Pacientes e insere na árvore ===
    novo_paciente = Pacientes(nome, idade, sexo, cpf, email, estudo_escolhido)
    arvore.inserir(novo_paciente)
    
    # === Salvando no arquivo JSON de pacientes ===
    caminho_paciente = 'app/data/pacientes/pacientes.json'
    if not os.path.exists(caminho_paciente) or os.path.getsize(caminho_paciente) == 0:
        users = []
    else:
        with open(caminho_paciente, "r", encoding="utf-8") as file:
            conteudo = file.read().strip()
            if not conteudo:
                users = []
            else:
                users = json.loads(conteudo)
                if not isinstance(users, list):
                    users = []
    
    users.append({
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "cpf": cpf,
        "email": email,
        "estudo": estudo_escolhido,
        "exames": [],
        "efeitos_adversos": []
    })
    
    with open(caminho_paciente, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=2, ensure_ascii=False)
    
    # === Salvando a ação no histórico ===
    user = getNameProfissional()
    historico_paciente = "app/data/historico_paciente/historico_paciente.json"
    historico = Historico(arquivo=historico_paciente)
    historico.registrarHistoricoPaciente(
        acao="Cadastro de paciente",
        paciente=novo_paciente.nome,
        email=novo_paciente.email,
        profissional=user['nome'],
        especializacao_prof=user['especializacao']
    )

# ========== Função auxiliar ============    
def getNameProfissional():
    caminho = 'app/data/users.json'
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding="utf-8") as file:
            users = json.load(file)
            for user in users:
                if user.get("isLogged") == 1:
                    return user
    return None


# ============ Validações ============
def validarEmail(email):
    if "@" in email and "." in email and "com" in email:
        return True
    print("\nEmail inválido")
    return False

def validarCpf(cpf):
    if len(cpf) < 11:
        print("Erro")
        return False
    return True
