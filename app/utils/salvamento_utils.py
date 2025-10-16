import json, os
from datetime import datetime

class Salvamento:
  def __init__(self, arquivo = None):
    self.arquivo = arquivo
    
    # Verifica se o arquivo existe,  e se o seu tamanho é igual a 0
    if not os.path.exists(self.arquivo) or os.path.getsize(arquivo) == 0:
      lista = []
      
      with open(self.arquivo, "w", encoding="utf-8") as file:
        json.dump(lista, file, indent=2, ensure_ascii=False)
        

  # Carrega o arquivo para salvar
  def _carregar(self):
    with open(self.arquivo, "r", encoding="utf-8") as file:
      conteudo = file.read().strip()
      
      if not conteudo:
        return []
      dados = json.loads(conteudo)
      if not isinstance(dados, list):
        return []
      return dados
    
  
  # Salva no no arquivo
  def _salvar(self, dados):
    with open(self.arquivo, "w", encoding="utf-8") as file:
      json.dump(dados, file, indent=2, ensure_ascii=False)
      
      
      
  def registrar_usuario(self, dados):
    usuario = {
      "Dados do Usuário": dados,
      "Data do salvamento":datetime.now().strftime("%d/%m/%y %H:%M:%S")
    }
    
    dados = self._carregar()
    dados.append(usuario)
    self._salvar(dados)
    
        
    