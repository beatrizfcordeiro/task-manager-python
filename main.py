import matplotlib.pyplot as plt

import json

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo) 
    except:
        return []
    
tarefas = carregar_tarefas()    

def adicionar_tarefa():
    titulo = input('Digite o título da tarefa: ')
    prioridade = input('Digite a prioridade (Baixa/Média/Alta): ')
    data_limite = input('Digite a data limite (DD/MM/AAAA): ')
    categoria = input('Digite a categoria: ')
    
    tarefa = {
        'titulo': titulo,
        'concluida': False,
        'prioridade': prioridade,
        'data_limite': data_limite,
        'categoria': categoria
    }

    return tarefa

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada.')
        return
    for i, tarefa in enumerate(tarefas):
        status =  '✅' if tarefa ['concluida'] else '❌'
        print(f"{i} - {tarefa['titulo']}[{status}]")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    try:
        indice = int(input('Digite o número da tarefa: '))

        if 0<= indice < len(tarefas):
            tarefas[indice]['concluida'] = True
            print('Tarefa concluída!')
        else:
            print('Índice inválido.')
    
    except:
        print('Entrada inválida.')

def deletar_tarefa(tarefas):
    listar_tarefas(tarefas)

    try:
        indice = int(input('Digite o número da tarefa: '))

        if 0<= indice < len(tarefas):
            tarefas.pop(indice)
            print('Tarefa deletada com sucesso!')
        else: 
            print('Índice inválido.')

    except:
        print('Entrada inválida.')


def mostrar_estatisticas(tarefas):
    total = len(tarefas)

    if total == 0:
        print("Nenhuma tarefa cadastrada.")
        return
    
    concluidas = 0 

    for tarefa in tarefas:
        if tarefa["concluida"]:
            concluidas += 1

    pendentes = total - concluidas
    porcentagem = (concluidas/total)*100

    print("\n Estatísticas:")
    print(f"Total de tarefas: {total}.")
    print(f"Concluídas: {concluidas}.")
    print(f"Pendentes: {pendentes}.")
    print(f"Progresso: {porcentagem:.2f}%.")

def gerar_grafico(tarefas):
    total = len(tarefas)

    if total == 0:
        print("Nehuma tarefa para mostrar.")
        return
    
    concluidas = 0

    for tarefa in tarefas:
        if tarefa["concluida"]:
            concluidas += 1
    
    pendentes = total - concluidas

    labels = ['Concluídas', 'Pendentes']
    valores = [concluidas, pendentes]

    plt.figure()
    plt.bar(labels, valores)
    plt.title("Status das tarefas")
    plt.xlabel("Tipo")
    plt.ylabel("Quantidade")

    plt.savefig("grafico.png")
    plt.close()

    print('Gráfico salvo como grafico.png')   

while True:
    print('\n1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - Concluir tarefa')
    print('4 - Deletar tarefa')
    print('5 - Mostrar estatísticas')
    print('6 - Gerar gráfico')
    print('7 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nova_tarefa = adicionar_tarefa()
        tarefas.append(nova_tarefa)
        salvar_tarefas(tarefas)

    elif opcao == '2':
        listar_tarefas(tarefas)

    elif opcao == '3':
        concluir_tarefa(tarefas)
        salvar_tarefas(tarefas)

    elif opcao == '4':
        deletar_tarefa(tarefas)
        salvar_tarefas(tarefas)

    elif opcao == '5':
        mostrar_estatisticas(tarefas)

    elif opcao == '6':
        gerar_grafico(tarefas)

    elif opcao == '7':
        print('Saindo...')
        break

    else:
        print('Opção inválida.')


