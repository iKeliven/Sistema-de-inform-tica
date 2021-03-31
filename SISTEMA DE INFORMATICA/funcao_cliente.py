#funcao menu do cliente
def menu_cliente():
    print("MENU CLIENTES \n"
          "Escolha a opção: \n"
          "1 - Cadastrar cliente \n"
          "2 - Buscar Cliente \n"
          "3 - Listar Clientes \n"z
          "4 - Alterar Cliente \n"
          "5 - Excluir Cliente \n"
          "6 - Fazer uma Cópia \n"
          "Digite a opção: ")
    return input()

#funcao validação do menu do cliente
def validar_menu_cliente():
    while True:
        opcao = menu_cliente()
        if opcao == "1":
            cadastro_cliente()
        elif opcao == "2":
            cpf_c = input("Digite o CPF do cliente: ")
            buscar_cliente(cpf_c)
        elif opcao == "3":
            listar_cliente()
        elif opcao == "4":
            cpf_c = input("Digite o CPF do cliente: ")
            alterar_cliente(cpf_c)
        elif opcao == "5":
            cpf_c = input("Digite o CPF do cliente: ")
            excluir_cliente(cpf_c)
        elif opcao == "6":
            copia_cliente()
        else:
            print("Programa Finalizado!")
            break


#funcao cadastro cliente
def cadastro_cliente():
    try:
        arquivo = open("Dados_Clientes.txt", "a")
        print("Cadastrar Cliente: ")
        nome_c = input("Nome completo: ").title()
        cpf_c = input("CPF: ")
        nascimento_c = input("Data de Nascimento: ")
        telefone_c = input("Telefone: ")
        endereco_c = input("Endereço: ")
        arquivo.write(cpf_c + " # " + nome_c + " # " + nascimento_c + " # " + telefone_c + " # " + endereco_c + "\n")
        arquivo.close()
        print("Cliente cadastrado com sucesso!")
    except IOError as error:
        print("Erro: ", error)

#funcao pesquisar cliente
def buscar_cliente(cpf_c):
    try:
        arquivo = open("Dados_Clientes.txt", "r+")
        for linha in arquivo:
            linha = linha.rstrip()
            if cpf_c in linha:
                print(linha)
            else:
                print("Cliente não encontrado!")
                cadastro_cliente()
        arquivo.close()
    except IOError as error:
        print("Erro: ", error)


#funcao listar cliente
def listar_cliente():
    try:
        arquivo = open("Dados_Clientes.txt", "r+")
        print("Lista de clientes: \n")
        for linhas in arquivo:
            linhas = linhas.rstrip() #funcao para tirar o enter vazio
            print(linhas)
        arquivo.close()
    except IOError as error:
        print("Erro: ", error)

# funcao alterar cliente
def alterar_cliente(cpf_c):
    try:
        with open('Dados_Clientes.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for elemento in linhas:
                if elemento.startswith(cpf_c):
                    print("Alterar Cliente: ")
                    nome_c = input("Nome completo: ").title()
                    cpf_c = input("CPF: ")
                    nascimento_c = input("Data de Nascimento: ")
                    telefone_c = input("Telefone: ")
                    endereco_c = input("Endereço: ")
                    pos = linhas.index(elemento)
                    item_c = (cpf_c + '#' + nome_c + '#' + nascimento_c + '#' + telefone_c + '#' + endereco_c + '\n')
                    linhas.pop(pos)
                    linhas.insert(pos, item_c)
                    arquivo = open('Dados_Clientes.txt', 'w')
                    arquivo.writelines(linhas)
                    arquivo.close()
                    print("Alteração realizada com sucesso!")
    except IOError as error:
        print('Erro', error)



# funcao excluir cliente
def excluir_cliente(cpf_c):
    try:
        arquivo = open("Dados_Clientes.txt", "r")
        linhas = arquivo.readlines()
        for elemento in linhas:
            if elemento.startswith(cpf_c):
                pos = linhas.index(elemento)
                linhas.pop(pos)
                arquivo = open("Dados_Clientes.txt", "w")
                arquivo.writelines(linhas)
        arquivo.close()
        print("Cliente removido! \n")
        return 0
    except IOError as error:
        print("ERRO: ", error)

#funcao copia cliente
def copia_cliente():
    try:
        arquivo1 = open("Dados_Clientes.txt", "r")
        arquivo2 = open("copia_Dados_Clientes.txt", "w")
        for texto in arquivo1:
            arquivo2.write(texto)
        arquivo1.close()
        arquivo2.close()
    except IOError as error:
        print("ERRO: ", error)









