import json, os
from datetime import datetime
from app.auth.menu.register_paciente import arvore
from app.utils.historico_utils import Historico

# === Define os impactos ambientais por tipo de exame
impactos_ambientais = {
    "Eletrocardiograma": {"papel": 1, "energia_kwh": 0.5, "residuo_reagente": 0},
    "Holter": {"papel": 0, "energia_kwh": 1, "residuo_reagente": 5},
    "Mapa": {"papel": 1, "energia_kwh": 0.7, "residuo_reagente": 2}
}


# === Registrar impacto ambiental ===
def registrar_impacto(exame_tipo, usuario):
    impacto = impactos_ambientais.get(exame_tipo)
    if not impacto:
        print("\nExame não cadastrado para rastreio ambiental")
        return

    registro = {
        "usuario": usuario,
        "exame": exame_tipo,
        "impacto": impacto,
        "Data da ação": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    caminho_impacto = "app/data/impactos_ambientais.json"
    dados = []

    if os.path.exists(caminho_impacto) and os.path.getsize(caminho_impacto) > 0:
        with open(caminho_impacto, "r", encoding="utf-8") as file:
            try:
                dados = json.load(file)
                if not isinstance(dados, list):
                    dados = []
            except json.JSONDecodeError:
                dados = []

    dados.append(registro)

    with open(caminho_impacto, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=2, ensure_ascii=False)



# === Gerar relatório de impactos ambientais ===
def gerar_relatorio_ambiental():
    caminho_impactos = "app/data/impactos_ambientais.json"

    if not os.path.exists(caminho_impactos) or os.path.getsize(caminho_impactos) == 0:
        print("\nNenhum impacto registrado ainda.")
        return

    with open(caminho_impactos, "r", encoding="utf-8") as file:
        try:
            impactos = json.load(file)
            if not isinstance(impactos, list):
                impactos = []
        except json.JSONDecodeError:
            impactos = []

    if not impactos:
        print("\nNenhum impacto registrado ainda.")
        return

    print("\n=== RELATÓRIO DE IMPACTOS AMBIENTAIS ===")
    for reg in impactos:
        usuario = reg.get("usuario", "Desconhecido")
        exame = reg.get("exame", "Desconhecido")
        impacto = reg.get("impacto", {})
        data = reg.get("Data da ação", "Não informado")
        print(f"Paciente: {usuario}")
        print(f"Exame: {exame}")
        print(f"Data: {data}")
        print(f"Impacto: Papel {impacto.get('papel', 0)} un, Energia {impacto.get('energia_kwh', 0)} kWh, Resíduos {impacto.get('residuo_reagente', 0)} ml")




# === Registrar exames ===
def registrar_exames():
    user = getLoggedProfissional()
    
    print("\n--- REGISTRAR EXAME ---")
    nome = input("Nome do Paciente: ")
    paciente = arvore.buscar(nome)
    if not paciente:
        print("\nPaciente não encontrado na arvore")
        return

    tipo = input("Tipo de exame (Eletrocardiograma, Holter, Mapa): ")
    resultado = input("Resultado do exame: ")

    exame = {"tipo": tipo, "resultado": resultado}
    paciente.exames.append(exame)
    print(f"Exame {tipo} registrado para o paciente {paciente.nome}")

    # Salva impacto ambiental
    registrar_impacto(tipo, paciente.nome)

    # === Salvar no JSON de pacientes ===
    caminho_paciente = "app/data/pacientes/pacientes.json"
    if os.path.exists(caminho_paciente):
        with open(caminho_paciente, "r", encoding="utf-8") as file:
            pacientes_json = json.load(file)

        for p in pacientes_json:
            if p["nome"] == paciente.nome:
                p["exames"] = paciente.exames

        with open(caminho_paciente, "w", encoding="utf-8") as file:
            json.dump(pacientes_json, file, indent=2, ensure_ascii=False)
            
            
    historico_exame = "app/data/estudos_clinicos/exames.json"
    historico = Historico(arquivo=historico_exame)
    historico.registrar(acao="Registro de exame", usuario=user["nome"])



# === Registrar efeitos adversos ===
def registrar_efeito_adversos():
    user = getLoggedProfissional()  
    print("\n--- REGISTRAR EFEITO ADVERSOS ---")
    nome = input("Nome do paciente: ")
    paciente = arvore.buscar(nome)
    if not paciente:
        print("\nPaciente não encontrado na árvore")
        return

    descricao = input("Descreva o efeito adverso: ")
    gravidade = input("Gravidade (Leve / Moderado / Grave): ")
    efeito = {"descricao": descricao, "gravidade": gravidade}

    paciente.efeitos_adversos.append(efeito)
    print(f"Efeito adverso registrado para o paciente {paciente.nome}")

    # Atualizar JSON
    caminho_paciente = "app/data/pacientes/pacientes.json"
    if os.path.exists(caminho_paciente):
        with open(caminho_paciente, "r", encoding="utf-8") as file:
            pacientes_json = json.load(file)

        for p in pacientes_json:
            if p["nome"] == paciente.nome:
                p["efeitos_adversos"] = paciente.efeitos_adversos

        with open(caminho_paciente, "w", encoding="utf-8") as file:
            json.dump(pacientes_json, file, indent=2, ensure_ascii=False)
            
    
    # Salvando a ação no histórico
    historico_efeitos = "app/data/estudos_clinicos/efeitos_adversos.json"
    historico = Historico(arquivo=historico_efeitos)
    historico.registrar(acao="Registro de efeitos adversos", usuario=user["nome"])

# === Visualizar paciente ===
def visualizar_paciente():
    print("\n--- VISUALIZAR PACIENTE ---")
    nome = input("Nome do paciente: ")
    paciente = arvore.buscar(nome)
    if not paciente:
        print("\nPaciente não encontrado na arvore")
        return

    print(f"\n--- Dados do paciente: {paciente.nome} ---")
    print(f"Idade: {paciente.idade}")
    print(f"Sexo: {paciente.sexo}")
    print(f"CPF: {paciente.cpf}")
    print(f"Email: {paciente.email}")
    print(f"Estudo Vinculado: {paciente.estudo}")

    print("\n=== EXAMES REGISTRADOS ===")
    if paciente.exames:
        for res in paciente.exames:
            print(f" - {res['tipo']}: {res['resultado']}")
    else:
        print("Nenhum exame registrado ainda")

    print("\n=== EFEITOS ADVERSOS ===")
    if paciente.efeitos_adversos:
        for p_efeito in paciente.efeitos_adversos:
            print(f" - {p_efeito['descricao']} ({p_efeito['gravidade']})")
    else:
        print("Nenhum efeito adverso registrado")
        
        
        
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
