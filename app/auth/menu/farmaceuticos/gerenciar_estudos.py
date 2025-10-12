import json
import os
from app.utils.historico_utils import Historico

CAMINHO_ESTUDOS = "app/data/estudos_clinicos/estudos_salvos.json"

def gerenciar_estudos():
    while True:
        print("\n--- GERENCIAR ESTUDOS FARMACÊUTICOS ---")
        print("1 - Listar estudos")
        print("2 - Remover estudo")
        print("3 - Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            listar_estudos()
        elif opcao == "2":
            remover_estudo()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")


# === Listar estudos ===
def listar_estudos():
    estudos = carregar_estudos()
    if not estudos:
        print("\nNenhum estudo cadastrado.")
        return
    print("\nEstudos cadastrados:")
    for i, est in enumerate(estudos, 1):
        print(f"{i} - {est['nome']}")


# === Remover estudo ===
def remover_estudo():
    user = getLoggedProfissional()
    
    estudos = carregar_estudos()
    if not estudos:
        print("\nNenhum estudo cadastrado.")
        return
    listar_estudos()
    try:
        escolha = int(input("Escolha o número do estudo para remover: "))
        if escolha < 1 or escolha > len(estudos):
            print("Escolha inválida.")
            return
    except ValueError:
        print("Opção inválida.")
        return
    estudo_removido = estudos.pop(escolha - 1)
    salvar_estudos(estudos)
    print(f"\nEstudo '{estudo_removido['nome']}' removido com sucesso.")
    
    
    # Salvando a ação no historico
    historico_estudos = "app/data/historico_user/historico_estudo.json"
    historico = Historico(arquivo=historico_estudos)
    historico.registrar(acao="Remoção de Estudo", usuario=user["nome"])


# === Funções auxiliares para JSON ===
def carregar_estudos():
    if not os.path.exists(CAMINHO_ESTUDOS) or os.path.getsize(CAMINHO_ESTUDOS) == 0:
        return []
    with open(CAMINHO_ESTUDOS, "r", encoding="utf-8") as file:
        try:
            estudos = json.load(file)
            if not isinstance(estudos, list):
                return []
            return estudos
        except json.JSONDecodeError:
            return []

def salvar_estudos(estudos):
    with open(CAMINHO_ESTUDOS, "w", encoding="utf-8") as file:
        json.dump(estudos, file, indent=2, ensure_ascii=False)
        
        
# === Codigo auxiliar ===
def getLoggedProfissional():
  caminho = 'app/data/users.json'
  
  if os.path.exists(caminho):   
    with open(caminho, 'r') as file: 
      users = json.load(file) 
      for user in users: 
        if user.get("isLogged") == 1: 
          return user 
  return None 
