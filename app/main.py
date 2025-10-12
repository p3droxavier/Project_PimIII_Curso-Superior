# Entrada do sistema

from app.auth.register import registerProfissional
from app.auth.login import login

# === UI interface de interação Profissional ===
def home():

  while True:
    print("\n=== Olá, Bem Vindo! ===")
    print("Digite: \n1 - Logar\n2 - Cadastrar\n3 - Encerrar o programa")
    option = input("-> ")
    # Para fazer o login no sistema
    if option == "1":
      login()
    # Para Cadastrar o usuário (profissional) no sistema
    elif option == "2":
      registerProfissional()
    # Encerra o programa 
    elif option == "3":
      print("Encerrando o programa")
      break
    
    else:
      print("Opção inválida! Tente novamente mais tarde.")
  

# Serve para poder rodar o sistema a partir desse arquivo
if __name__ == "__main__":
  home()

