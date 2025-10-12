"""
O paciente sera conectado a um estudo ja existente. 
Dessa forma, sera conectado a arvore binária.
"""

import json, os

class Pacientes:
  def __init__(self, nome, idade, sexo, cpf, email, estudo=None):
    self.nome = nome
    self.idade = idade
    self.sexo = sexo
    self.cpf = cpf
    self.email = email
    self.estudo = estudo
    self.exames = []
    self.efeitos_adversos = []
    self.esquerda = None
    self.direita = None
    
  # Atualiza a fase do estudo do paciente
  def atualizar_fase(self, nova_fase):
    if isinstance(self.estudo, dict):
      self.estudo["fase"] = nova_fase
      print(f"\nFase do estudo atualizado para: {nova_fase}")
      
    else:
      print("\nPaciente não possui estado associado.")
    

# Classe da arvore binaria de pacientes
class ArvorePaciente:
  def __init__(self):
    self.raiz = None
    
  # Insere o paciente na arvore 
  def inserir(self, paciente):
    if self.raiz is None:
      self.raiz = paciente
      
    else:
      self._inserir(self.raiz, paciente)
      
      
  def _inserir(self, atual, novo):
    if novo.nome.lower()< atual.nome.lower():
      if atual.esquerda is None:
        atual.esquerda = novo
        
      else:
        self._inserir(atual.direita, novo)
        
    else: 
      if atual.direita is None:
        atual.direita = novo
        
      else: 
        self._inserir(atual.direita, novo)
        
        
  def buscar(self, nome):
    return self._buscar(self.raiz, nome)
        
        
  def _buscar(self, atual, nome):
    if atual is None:
      return None
    
    if atual.nome.lower() == nome.lower():
      return atual
    
    elif nome.lower() < atual.nome.lower():
      return self._buscar(atual.esquerda, nome)
    
    else:
      return self._buscar(atual.direita, nome)
    
    
    
 # Listar pacientes
  def listar_pacientes(self):
      print("\n=== Lista de pacientes cadastrados ===")
      if not self.raiz:
          print("Nenhum paciente na árvore.")
          return
      self._listar_pacientes(self.raiz)

  def _listar_pacientes(self, atual):
      if atual:
          self._listar_pacientes(atual.esquerda)
          
          # Mostra o nome do estudo ou faze, se houver
          if isinstance(atual.estudo, dict):
              nome_estudo = atual.estudo.get("nome", " ")
              fase_estudo = atual.estudo.get("fase", "")
              print(f" - {atual.nome} ({nome_estudo} - {fase_estudo})")
            
          else:
            print(f" - {atual.nome} ({atual.estudo or 'Sem estudo associado'})")
            
          self._listar_pacientes(atual.direita)


  #  Carregar pacientes salvos do JSON
  def carregar_de_json(self, caminho='app/data/pacientes/pacientes.json'):
      """Carrega pacientes salvos no arquivo JSON e insere na árvore."""
      if not os.path.exists(caminho) or os.path.getsize(caminho) == 0:
          print("\n Nenhum paciente salvo ainda.")
          return

      with open(caminho, "r", encoding="utf-8") as file:
          try:
              pacientes = json.load(file)
              if not isinstance(pacientes, list):
                  print("\nEstrutura inválida no JSON de pacientes.")
                  return
          except json.JSONDecodeError:
              print("\nErro ao ler o arquivo JSON.")
              return

      for p in pacientes:
          paciente = Pacientes(
              nome=p.get("nome"),
              idade=p.get("idade"),
              sexo=p.get("sexo"),
              cpf=p.get("cpf"),
              email=p.get("email"),
              estudo=p.get("estudo", None)
          )
          self.inserir(paciente)

      print(f"\n {len(pacientes)} pacientes carregados na árvore com sucesso.")
      