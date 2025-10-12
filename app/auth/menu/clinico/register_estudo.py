import os
import json
from app.auth.menu.clinico.arvore_paciente import Pacientes, ArvorePaciente
from app.utils.historico_utils import Historico

arvore = ArvorePaciente()
arvore.carregar_de_json()

def cadastrar_estudos():
  print("--- Cadastrar um novo estudo Clínico ---")
  nome = input("Nome do estudo: ")
  medicamento = input("Medicamento ou/e teste: ")
  objetivo = input("Qual o objetivo: ")
  
  
  novos_estudo = {
    "nome":nome,
    "medicamento":medicamento,
    "objetivo":objetivo,
    "status":"Ativo",
    "exames":[] # Aqui serão guardados os exames que seram feitos
  }
  
  caminho = "app/data/estudos_clinicos/estudos_salvos.json"
  
  if not os.path.exists(caminho) or os.path.getsize(caminho) == 0:
    estudos = []
    
  else:
    with open(caminho, "r", encoding="utf-8") as file:
      conteudo = file.read().strip()
      
      if not conteudo:
        estudos = []
        
      else:
        estudos = json.loads(conteudo)
        if not isinstance(estudos, list):
          estudos = []
          
  estudos.append(novos_estudo)
  novos_estudo
  
  with open(caminho, "w", encoding="utf-8") as file:
    json.dump(estudos, file, indent=2, ensure_ascii=False)
    
    
  # === Salvando a ação de criar um estudo ===
  user = getNameProfissional()
  historico_estudo = "app/data/historico_user/historico_estudo.json"
  historico = Historico(arquivo=historico_estudo)
  historico.registrarMedicamento(acao="Cadastro de estudos Clinicos", usuario=user["nome"], medicamento=novos_estudo["medicamento"])
  
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
  