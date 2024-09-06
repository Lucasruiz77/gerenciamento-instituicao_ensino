'''
Lucas Henrique Oliveira Ruiz | Análise e Desenvolvimento de Sistemas
'''



#Criação de uma variavel para armazenar a listagem de alunos 
estudantes = [] 

# Primeiro while verificando uma condição verdadeira no primeiro menu

while True:

    #Print do menu principal
    print ("---- MENU PRINCIPAL ----\n")
    print ("[1] Gerenciar Estudantes.")
    print ("[2] Gerenciar Disciplinas.")
    print ("[3] Gerenciar Professores.")
    print ("[4] Gerenciar Turmas.")
    print ("[5] Gerenciar Matrículas") 
    print ("[9] Sair\n")

    #Pergunta ao usuario qual a opção deseja dentro do menu principal
    opcao = int(input("Informe a opção desejada: "))

    if opcao == 9:# Condição para sair do programa
        print ("\nFinalizando a aplicação...")
        break

    #Segundo While verifica uma condição verdadeira no menu de operações
    while True:
        if opcao == 1:
            print ("\n\n***** [ESTUDANTES] MENU DE OPERAÇÕES *****\n")             
        elif opcao == 2:
            print ("\n\nEM DESENVOLVIMENTO\n") 
            break           
        elif opcao == 3:
            print ("\n\nEM DESENVOLVIMENTO\n")  
            break           
        elif opcao == 4:
            print ("\n\nEM DESENVOLVIMENTO\n")
            break
        elif opcao == 5:
            print("\n\nEM DESENVOLVIMENTO\n")
            break
        else:
            print("\n\nOpção inválida")# Sai do segundo loop para voltar ao menu principal
            break 

        #Print do menu secúndário após perguntar a condição acima, a condição dita o cabeçalho.

        print ("[1] Incluir.")
        print ("[2] Listar.")
        print ("[3] Atualizar.")
        print ("[4] Excluir.")
        print ("[9] Voltar ao menu principal.\n")

        #Pergunta a ação que o usuario deseja no menu secúndario

        acao = int(input("Informe a ação desejada: ")) 

        #Criação de uma condição para a escolha da ação

        if acao == 1: #Condição inclui cada aluno digitado na lista da variavel estudantes = []
            print("\n\n===== INCLUSÃO =====\n")
            nome = input("Informe o nome do Estudante: ")
            print("Pressione ENTER para continuar")
            input()
            estudantes.append(nome)
        elif acao == 2: #Condição printa os alunos que estão dentro da lista estudantes = [], caso não tenha alunos cadastrados será printado a frase "Não há estudantes cadastrados."
            print("\n\n===== LISTAGEM =====\n")
            for i in estudantes:
                print (i)
            print("\nPressione ENTER para continuar")
            input()
            if len(estudantes) == 0:
                    print ("Não há estudantes cadastrados.")  
        elif acao == 3:
            print("\n\nEM DESENVOLVIMENTO\n")
            break
        elif acao == 4:
            print("\n\nEM DESENVOLVIMENTO\n")
            break
        elif acao == 9: # Voltar ao menu principal
            print("\n\nVocê voltou para o menu principal\n")
            break
        else:
            print("\n\nOpção inválida!")
