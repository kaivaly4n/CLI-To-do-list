#Sistema Gerenciador de Tarefas
# Apresentação do sistema e primeira interação com o usuário
input(f"Olá, este é seu Gerenciador de Tarefas!\nAperte Enter para começar...")

""" 
Função: Adicionar tarefas ao sistemam, reunindo os inputs do usuário de: nome da tarefa,
descrição da tarefa e urgência, e em seguida confirmando que a tarefa foi adicionada.
"""

tarefas = []
def adicionar_tarefa():
  nome = input("Digite o nome da tarefa: ")
  descricao = input("Digite a descrição da tarefa: ")
  urgencia = int(input("Digite a urgência da tarefa (1 - Alta, 2 - Média, 3 - Baixa): "))
  tarefas.append({"Nome": nome, "Descrição": descricao, "Urgência": urgencia, "Concluída": False})
  print("Tarefa adicionada!")

"""
Função: Listar todas as tarefas cadastradas, enumerando-as e às exibindo junto com seus metadados.
Se não ouver tarefas disponíveis, avisa o usuário disso.
"""

def listar_tarefas():
  print(f"\nTarefas: ")
  if tarefas:
     for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["Concluída"] else "Afazer"
        print(f"{i}. Nome: {tarefa['Nome']} | Descrição: {tarefa['Descrição']} | Urgência: {tarefa['Urgência']} | Status: {status}")
  else:
      print("Não há tarefas disponíveis.")


""" 
Função: Marcar tarefa como concluída. Essa função interage com a função listar_tarefas,
relacionando o input do usuário com o booleano de status, alterando-o para True.
"""

def marcar_tarefa_concluida():
  listar_tarefas()
  if tarefas:
      tarefa_concluida = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
      if 0 <= tarefa_concluida < len(tarefas):
          tarefas[tarefa_concluida] ["Concluída"] = True       
          print(f"Tarefa marcada como concluída.")
      else:
          print("Tarefa não encontrada.")
  else:
      print("Não há tarefas disponíveis.")

"""
Função: Remover Tarefa. Essa função usa o input do usuário para interagir
com a lista de tarefas, removendo a opção escolhida.
"""

def remover_tarefa():
    listar_tarefas()
    if tarefas:
        tarefa_removida = int(input("Digite o número da tarefa que deseja remover: ")) -1
        if 0 <= tarefa_removida < len(tarefas):
            del tarefas[tarefa_removida]
            print(f"Tarefa removida.")
        else:
            print("Tarefa não encontrada.")
    else:
       print("Não há tarefas. Adicione uma agora!")

"""
Menu em forma de loop While 
"""

while True:
  print(f"\nMENU\n")
  print("1. Adicionar tarefas")
  print("2. Listar tarefas")
  print("3. Marcar tarefa como concluída")
  print("4. Remover Tarefa")
  print("5. Sair")


  escolha = input(f"Digite o número correspondente a opção desejada (1-5): \n")
  if escolha == "1":
    adicionar_tarefa()
  elif escolha == "2":
    listar_tarefas()
  elif escolha == "3":
    marcar_tarefa_concluida()
  elif escolha == "4":
    remover_tarefa()
  elif escolha == "5":
    print("Tchau Tchau!")
    break
  else:
    print("Opção inválida. Insira uma opção entre (1-5).")
