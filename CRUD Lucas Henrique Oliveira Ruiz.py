'''
Lucas Henrique Oliveira Ruiz | Análise e Desenvolvimento de Sistemas
'''
# Criação de uma variável para armazenar a listagem de alunos
estudantes = []

# Primeiro while verificando uma condição verdadeira no primeiro menu
while True:
    # Print do menu principal
    print("---- MENU PRINCIPAL ----\n")
    print("[1] Gerenciar Estudantes.")
    print("[2] Gerenciar Disciplinas.")
    print("[3] Gerenciar Professores.")
    print("[4] Gerenciar Turmas.")
    print("[5] Gerenciar Matrículas")
    print("[9] Sair\n")

    # Pergunta ao usuário qual a opção deseja dentro do menu principal
    opcao = int(input("Informe a opção desejada: "))

    if opcao == 9:  # Condição para sair do programa
        print("\nFinalizando a aplicação...")
        break

    # Segundo While verifica uma condição verdadeira no menu de operações
    while True:
        if opcao == 1:
            print("\n\n***** [ESTUDANTES] MENU DE OPERAÇÕES *****\n")
        elif opcao == 2:
            print("\n\nEM DESENVOLVIMENTO\n")
            break
        elif opcao == 3:
            print("\n\nEM DESENVOLVIMENTO\n")
            break
        elif opcao == 4:
            print("\n\nEM DESENVOLVIMENTO\n")
            break
        elif opcao == 5:
            print("\n\nEM DESENVOLVIMENTO\n")
            break
        else:
            print("\n\nOpção inválida")  # Sai do segundo loop para voltar ao menu principal
            break

        # Print do menu secundário após perguntar a condição acima
        print("[1] Incluir.")
        print("[2] Listar.")
        print("[3] Atualizar.")
        print("[4] Excluir.")
        print("[9] Voltar ao menu principal.\n")

        # Pergunta a ação que o usuário deseja no menu secundário
        acao = int(input("Informe a ação desejada: "))

        # Criação de uma condição para a escolha da ação
        if acao == 1:  # Incluir estudante na lista
            print("\n\n===== INCLUSÃO =====\n")
            codigo = int(input("Digite o código do estudante: "))
            nome = input("Informe o nome do Estudante: ")
            cpf = input("Digite o CPF do estudante: ")
            input("Pressione ENTER para continuar")
            dados_estudante = {
                "codigo_estudante": codigo,
                "nome_estudante": nome,
                "cpf_estudante": cpf
            }
            estudantes.append(dados_estudante)
        elif acao == 2:  # Listar os estudantes
            print("\n\n===== LISTAGEM =====\n")
            if estudantes:
                for estudante in estudantes:
                    print("-", estudante)
                input("\nPressione ENTER para continuar")
            else:
                print("Não há estudantes cadastrados.")
        elif acao == 3:  # Atualizar estudante
            codigo_editar = int(input("Qual o código que você deseja editar: "))
            estudante_editado = None
            for estudante in estudantes:
                if estudante["codigo_estudante"] == codigo_editar:
                    estudante_editado = estudante
                    break
            if estudante_editado is None:
                print(f"O código {codigo_editar} não foi encontrado.")
            else:
                estudante_editado["codigo_estudante"] = int(input("Digite o novo código: "))
                estudante_editado["nome_estudante"] = input("Digite o novo nome: ")
                estudante_editado["cpf_estudante"] = input("Digite o novo CPF: ")
                print("Estudante atualizado com sucesso.")
        elif acao == 4:  # Excluir estudante da lista
            codigo_excluir = int(input("Qual o código que você deseja excluir? "))
            estudante_removido = None
            for estudante in estudantes:
                if estudante["codigo_estudante"] == codigo_excluir:
                    estudante_removido = estudante
                    break
            if estudante_removido:
                estudantes.remove(estudante_removido)
                print(f"Estudante {estudante_removido['nome_estudante']} removido com sucesso.")
            else:
                print("Estudante não encontrado.")
        elif acao == 9:  # Voltar ao menu principal
            print("\n\nVocê voltou para o menu principal\n")
            break
        else:
            print("\n\nOpção inválida!\n")
