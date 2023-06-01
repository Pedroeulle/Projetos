# PROJETO 2: GERENCIADOR DE TAREFAS
# Introdução:
# Neste projeto, você irá criar um aplicativo de linha de comando que permitirá aos usuários gerenciar suas tarefas diárias. O objetivo é criar um sistema simples de gerenciamento de tarefas, onde os usuários poderão adicionar, remover e exibir tarefas.

# OQUE FAZER:

listaTarefas = [] # sempre que uma informação for para ser adiconada a uma lista a mesma precisa estar fora do loop pois ela sera sempre zerada ao final do loop

while True:

  # Crie um menu inicial que exiba as opções disponíveis para o usuário: adicionar tarefa, remover tarefa e exibir tarefas.
  print ("ESCOLHA A OPÇÃO QUE DESEJA REALIZAR:\n\n1 - Adicionar Tarefa\n2 - Remover Tarefa\n3 - Exibir Tarefas\n4 - Fechar\n")

# Solicite ao usuário que escolha uma das opções do menu.
  menuInicial = int(input("Digite o numero da opção desejada: "))
  
# Dependendo da opção escolhida, implemente a lógica correspondente para adicionar tarefas.
  if menuInicial == 1:
    novaTarefa = input("\nDigite a tarefa: ").capitalize()
    listaTarefas.append(novaTarefa)
    print("\nLISTA DE TAREFAS:\n")
    for indiceLista, elementoLista in enumerate(listaTarefas):
      print(indiceLista+1 , elementoLista , "\n")

# Dependendo da opção escolhida, implemente a lógica correspondente remover tarefas.
  elif menuInicial == 2 :
    print("\nLISTA DE TAREFAS:\n")
    for indiceLista, elementoLista in enumerate(listaTarefas):
      print(indiceLista+1 , elementoLista , "\n")
    remover = int(input("Digite o numero da tarefa que deseja remover: "))
    remover = listaTarefas.pop(remover-1)
     if remover >= 1 and remover <= len(listaTarefas):
        tarefaRemovida = listaTarefas.pop(remover-1)
                print(f"A tarefa '{tarefaRemovida}' foi removida com sucesso.\n")
            else:
                print("\nTarefa inválida. Por favor, digite um número válido.\n")
# Dependendo da opção escolhida, implemente a lógica correspondente para exibir tarefas.
  elif menuInicial == 3:
    print("\nLISTA DE TAREFAS:\n")
    for indiceLista, elementoLista in enumerate(listaTarefas):
      
      print(indiceLista+1 , elementoLista , "\n")
# Continue exibindo o menu enquanto o usuário não escolher sair do programa.
  elif menuInicial == 4:
    print("\nObrigado por usar o programa, ate logo :)\n")
    break
    
# Adicione tratamento de erros para lidar com possíveis situações, como tentar remover uma tarefa que não existe ou fazer uma escolha inválida no menu.
  else:
    print("\nVALOR INVALIDO TENTE NOVAMENTE\n")