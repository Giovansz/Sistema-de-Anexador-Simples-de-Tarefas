# Criar um programa simples em Python que funcione como um gerenciador de tarefas. O programa permitirá que o usuário   adicione, visualize e remova tarefas de uma lista. 

# Adicionar Tarefas: O usuário deve ser capaz de adicionar uma nova tarefa à lista. Cada tarefa deve ter um título e uma descrição.

Tarefas = []
def adicionar():
    try:
        nome = str(input('Digite o nome da tarefa: '))
        if nome == '':
            print('O nome da atividade não pode ser vazio.')
            return
    
        descriçao = input('Descrição da atividade: ')
        if descriçao == '':
            print('a descrição da atividade não pode ser vazio.')
            return
    except ValueError:
        print('Apenas letras e palavras')

    tarefa = {
        "nome": nome,
        "descrição": descriçao
    }
    Tarefas.append(tarefa)
    print(f'{nome} adicionada com sucesso!')

# Visualizar Tarefas: O usuário deve poder visualizar todas as tarefas adicionadas, mostrando o título e a descrição.
def visualizar():
    if not Tarefas:
        print('Sem tarefas cadastradas!')
        return
    else:
        print('Tarefas cadastradas: \n')
        for i,tarefa in enumerate(Tarefas, start=1):
            print(f'{i}. {tarefa['nome']}: {tarefa['descrição']}')
            print(25 * '-')

# Remover Tarefas: O usuário deve ser capaz de remover uma tarefa da lista usando o título da tarefa.
def remover():
    if not Tarefas:
        print('Sem tarefas cadastradas!')
        return
    visualizar()
    try:
        tarefa_removida = int(input('Qual tarefa deseja remover? '))
        if 1 <= tarefa_removida <= len(Tarefas):
            Tarefas.pop(tarefa_removida - 1)
            print('Tarefa removida com sucesso!')
        else:
            print('Número da tarefa inválido.')
            return
    except ValueError:
        print('Tarefa não existente!')

def inicial():
    while True:
        try:
            pergunta = int(input('Bem-vindo ao anexador de tarefas! O que deseja? \n'
            '(1). Adicionar tarefa \n'
            '(2). Visualizar tarefas \n'
            '(3). Remover tarefa \n'
            '(4). Encerrar/Sair \n'
            'Opção: \n'))
            if pergunta == 1:
                adicionar()
            elif pergunta == 2:
                visualizar()
            elif pergunta == 3:
                remover()
            elif pergunta == 4:
                if not Tarefas:
                    print('Sem tarefas cadastradas, encerrando terminal!')
                    break
                else:  
                    visualizar()
                    break
            else:
                print('Opção não reconhecida, tente novamente!')
        except ValueError:
            print('Insira um número entre 1 e 4.')
inicial()

# Salvar e Carregar Tarefas: As tarefas devem ser salvas em um arquivo texto (por exemplo, tarefas.txt) para que possam ser carregadas na próxima execução do programa.