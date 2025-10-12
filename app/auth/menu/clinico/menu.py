from app.auth.menu.clinico.register_estudo import cadastrar_estudos
from app.auth.menu.clinico.exames import registrar_exames, registrar_efeito_adversos, visualizar_paciente
from app.auth.menu.register_paciente import arvore

def estudos_clinicos():
  while True:
    
    print("\n=== MENU DE ESTUDOS CLÍNICOS ===")
    print("1 - Cadastrar novo estudo: ")
    print("2 - Listar pacientes (árvore binária): ")
    print("3 - Registrar exame: ")
    print("4 - Registrar efeito adverso: ")
    print("5 - Visualizar paciente completo: ")
    print("6 - Voltar: ")
    
    opcao = input("-> ")
    
    if opcao == "1":
        cadastrar_estudos()
    elif opcao == "2":
        arvore.listar_pacientes()
    elif opcao == "3":
        registrar_exames()
    elif opcao == "4":
        registrar_efeito_adversos()
    elif opcao == "5":
        visualizar_paciente()
    elif opcao == "6":
        break
    else:
      print("Opção invalida!")