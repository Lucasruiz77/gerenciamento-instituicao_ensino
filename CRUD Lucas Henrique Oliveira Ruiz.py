
while True:



    print ("---- MENU PRINCIPAL ----\n")
    print ("[1] Gerenciar Estudantes.")
    print ("[2] Gerenciar Disciplinas.")
    print ("[3] Gerenciar Professores.")
    print ("[4] Gerenciar Turmas.")
    print ("[5] Gerenciar Matrículas") 
    print ("[9] Sair\n")

    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        print ("\n\n***** [ESTUDANTES] MENU DE OPERAÇÕES *****\n")             
    elif opcao == 2:
        print ("\n\n***** [DISCIPLINAS] MENU DE OPERAÇÕES *****\n")            
    elif opcao == 3:
        print ("\n\n***** [PROFESSORES] MENU DE OPERAÇÕES *****\n")             
    elif opcao == 4:
        print ("\n\n***** [TURMAS] MENU DE OPERAÇÕES *****\n")
    elif opcao == 9:
        print ("Estou finalizando sua interação")
        break   
    else:
        print("\n\nOpção inválida")

    while True:
        print ("[1] Incluir.")
        print ("[2] Listar.")
        print ("[3] Atualizar.")
        print ("[4] Excluir.")
        print ("[9] Voltar ao menu principal.\n")              

        acao = int(input("Informe a ação desejada: "))

        if acao == 1:
            print("\n\n===== INCLUSÃO =====\n")
        elif acao == 2:
            print("\n\n===== LISTAGEM =====\n")
        elif acao == 3:
            print("\n\n===== ATUALIZAÇÃO =====\n")
        elif acao == 4:
            print("\n\n===== EXCLUSÃO =====\n")
        elif acao == 9:
            print("\n\nVocê voltou para o menu principal\n")
            break
        else:
            print("\n\nOpção incorreta!")

print ("Finalizando a aplicação...")

