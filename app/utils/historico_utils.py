import json
import os
from datetime import datetime

class Historico:
  def __init__(self, arquivo='historico_user.json'):
    self.arquivo = arquivo
    # Garante que o arquivo exixta 
    if not os.path.exists(self.arquivo):
      with open(self.arquivo, "w", encoding="utf-8") as file:
        json.dump([], file, indent=2, ensure_ascii=False)
  
  
  
  # Carregara o histórico do arquivos para poder salvar outros
  def _carregar(self):
    with open(self.arquivo, "r", encoding="utf-8") as file:
      conteudo = file.read().strip() # le o conteudo do arquivo
      if not conteudo: # se estiver vazio, retorna uma lista vazia
        return []
      dados = json.loads(conteudo)
      if not isinstance(dados, list):
        return []
      return dados
  
  
  
  # Salvar a lista de eventos. Escreve todas as listas de registros, incluindo novos eventos, para que fiquem armazenadas.
  def _salvar(self, dados):
    with open(self.arquivo, "w", encoding="utf-8") as file:
      json.dump(dados, file, indent=2, ensure_ascii=False)
  
  
  
  # Cria um novo evento, com usuário, acão e a data. E add a lista de eventos
  def registrar(self, acao, usuario):
    
    # Aqui guarda o que sera registrado a cada ação feita 
    registro = {
      "Usuário":usuario,
      "Ação Realizada":acao,
      "Data da ação":datetime.now().strftime("%d/%m/%y %H:%M:%S") # Salva no formato Dia, Mes, Ano | Hora, Minuto, Segundo
    }
    
    dados = self._carregar()
    dados.append(registro)
    self._salvar(dados)
    
    
  def registrarMedicamento(self, acao, usuario, medicamento):
    
    # Aqui guarda o que sera registrado a cada ação feita 
    registro = {
      "Usuário":usuario,
      "Ação Realizada":acao,
      "Medicamento Cadastrado": medicamento,
      "Data da ação":datetime.now().strftime("%d/%m/%y %H:%M:%S") # Salva no formato Dia, Mes, Ano | Hora, Minuto, Segundo
    }
    
    dados = self._carregar()
    dados.append(registro)
    self._salvar(dados)
    
    
    
  def registrarHistoricoPaciente(self, acao, paciente, email, profissional, especializacao_prof):
    registro = {
      "Acao Realizada":acao,
      "Paciente": paciente,
      "Email do paciente":email,
      "Profissional": profissional,
      "Especializacao do Profissional":especializacao_prof,
      "Data da ação":datetime.now().strftime("%d/%m/%y %H:%M:%S")
    }
    
    dados = self._carregar()
    dados.append(registro)
    self._salvar(dados)
  
  
  
  # Retorna todos os registros do histórico
  def listar(self):
    pass
  
  
  
  