class Menu:
    # in exercícios aula 8 de programação 2020/21
    def __init__(self):
        opcao = ''
        while opcao != '0':
            print('Menu:')
            print('1. Listar Utilizadores')
            print('2. Adicionar saldo')
            print('3. Alterar password')
            print('4. Iniciar aluguer')
            print('5. Concluir aluguer')
            print('6. Listar alugueres ativos')
            print('7. Listar viaturas disponíveis')
            print('8. Informações do sistema')
            print('9. Actividade por hora e dia da semana')
            opcao = input("Indique a sua opção: ")
            if opcao == "2":
                a.listar()
            elif opcao == "7":
                a.gravar("contactos.txt")
            elif opcao == "8":
                try:
                    a.ler("contactos.txt")
                except:
                    print("Não é possivel ler o ficheiro")


# Chama o menu
