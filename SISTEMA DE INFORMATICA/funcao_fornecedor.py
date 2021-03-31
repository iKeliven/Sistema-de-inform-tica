#funcao menu do fornecedor
def menu_fornecedor():
    print("Escolha a opção: \n"
          "1 - Cadastrar Fornecedor \n"
          "2 - Pesquisar Fornecedor \n"
          "3 - Listar Fornecedores \n"
          "4 - Alterar Fornecedor \n"
          "5 - Excluir Fornecedor \n"
          "6 - Fazer uma Cópia ")
    return input()

#funcao validação do menu do fornecedor
def validar_menu_fornecedor():
    while True:
        opcao = menu_fornecedor()
        if opcao == "1":
            cadastro_fornecedor()
        elif opcao == "2":
            cod_for = input("Digite o código do fornecedor: ")
            buscar_fornecedor(cod_for)
        elif opcao == "3":
            listar_fornecedor()
        elif opcao == "4":
            cod_for = input("Digite o código do fornecedor: ")
            alterar_produto(cod_for)
        elif opcao == "5":
            cod_for = input("Digite o código do fornecedor: ")
            excluir_produto(cod_for)
        elif opcao == "6":
            copia_produto()
        else:
            print ("Programa Finalizado!")
            break

#funcao cadastro fornecedor
def cadastro_fornecedor():
    try:
        arquivo = open("Dados_Fornecedor.txt", "a")
        print("Cadastrar Fornecedor: ")
        nome_for = input("Nome: ").title()
        cod_for = input("Código: ")
        telefone_for = input("Preço: ")
        email_for = input("E-mail: ")
        arquivo.write(cod_for + " # " + cnpj_for + " # " + nome_for + " # " + telefone_for + " # " + email_for + "\n")
        arquivo.close()
        print("Fornecedor cadastrado com sucesso!")
    except IOError as error:
        print("Erro: ", error)

#funcao pesquisar fornecedor
def buscar_fornecedor(cod_for):
    try:
        arquivo = open("Dados_Fornecedor.txt", "r+")
        contador= 0
        for linha in arquivo:
            linha = linha.rstrip()
            if cod_for in linha:
                contador +=1
                print(linha)
            else:
                print("Fornecedor não encontrado!")
                cadastro_fornecedor()
        arquivo.close()
    except IOError as error:
        print("Erro: ", error)

#funcao listar fornecedor
def listar_fornecedor():
    try:
        arquivo = open("Dados_Produtos.txt", "r+")
        print("Lista de produto: \n")
        for linhas in arquivo:
            print(linhas)
        arquivo.close()
    except IOError as error:
        print("Erro: ", error)


#funcao alterar fornecedor
def alterar_fornecedor(cod_for):
    try:
        with open("Dados_Fornecedor.txt", "r") as arquivo:
            linhas = arquivo.readlines(cod_for)
            for elemento in linhas:
                if elemento.startswith(cod_for):
                    print("Alterar Fornecedor: ")
                    cnpj_for = input("CNPJ: ")
                    nome_for = input("Nome: ").title()
                    cod_for = input("Código: ")
                    telefone_for = input("Preço: ")
                    email_for = input("E-mail: ")
                    item_for = (cod_for + " # " + cnpj_for + " # " + nome_for + " # " +  telefone_for + " # " +
                                email_for + "\n")
                    pos = linhas.index(elemento)
                    linhas.pop(pos)
                    linhas.insert(item_for)
                    arquivo = open("Dados_Fornecedor.txt", "w")
                    arquivo.writelines(linhas)
                    arquivo.close()
                    print("Alteração realizada com sucesso! :)")
                else:
                    print("Cliente não encontrado!")
    except IOError as error:
        print("Erro: ", error)

# funcao excluir fornecedor
def excluir_fornecedor(cod_for):
    try:
        arquivo = open("Dados_Fornecedor.txt", "r")
        linhas = arquivo.readlines()
        for elemento in linhas:
            if elemento.startswith(cod_for):
                pos = linhas.index(elemento)
                linhas.pop(pos)
                arquivo = open("Dados_Fornecedor.txt", "w")
                arquivo.writelines(linhas)
        arquivo.close()
        print("Fornecedor removido! \n")
        return 0
    except IOError as error:
        print("ERRO: ", error)


#funcao copia fornecedor
def copia_fornecedor():
    try:
        arquivo1 = open("Dados_Fornecedor.txt", "r")
        arquivo2 = open("copia_Dados_Fornecedor.txt", "a")
        for texto in arquivo1:
            arquivo2.write(texto)
        print("Arquivo dados fornecedor copiado com sucesso!")
        arquivo1.close()
        arquivo2.close()
    except IOError as error:
        print("ERRO: ", error)

validar_menu_fornecedor()
cadastro_fornecedor()
buscar_fornecedor(cod_for)
listar_fornecedor()
alterar_fornecedor(cod_for)
excluir_fornecedor(cod_for)
copia_fornecedor()

