#funcao menu do produto
def menu_produto():
    print("Escolha a opção: \n"
          "1 - Cadastrar Produto \n"
          "2 - Pesquisar Produto \n"
          "3 - Listar Produto \n"
          "4 - Alterar Produto \n"
          "5 - Excluir Produto \n"
          "6 - Fazer uma Cópia ")
    return input()

#funcao validação do menu do produto
def validar_menu_produto():
    while True:
        opcao = menu_produto()
        if opcao == "1":
            cadastro_produto()
        elif opcao == "2":
            cod_p = input("Digite o código do produto: ").title()
            buscar_produto(cod_p)
        elif opcao == "3":
            listar_produto()
        elif opcao == "4":
            cod_p = input("Digite o código do produto: ").title()
            alterar_produto(cod_p)
        elif opcao == "5":
            cod_p = input("Digite o código do produto: ") .title()
            excluir_produto(cod_p)
        elif opcao == "6":
            copia_produto()
        else:
            print ("Programa Finalizado!")
            break


#funcao cadastro produto
def cadastro_produto():
    try:
        arquivo = open("Dados_Produtos.txt", "a")
        print("Cadastrar Produto: ")
        nome_p = input("Nome: ").title()
        cod_p = input("Código: ").title()
        preco_p = input("Preço: ")
        arquivo.write(cod_p + " # " + nome_p + " # " + preco_p + " # " )
        arquivo.close()
        print("Produto cadastrado com sucesso!")
    except IOError as error:
        print("Erro: ", error)

#funcao pesquisar produto
def buscar_produto(cod_p):
    try:
        arquivo = open("Dados_Produtos.txt", "r")
        for linha in arquivo:
            if cod_p in linha:
                linha_lista = linha.split(" # ")
                print(linha_lista[1], "=", linha_lista[0], " Preço:", linha_lista[2])
            else:
                print("Produto não encontrado!")
                cadastro_produto()
        arquivo.close()
    except IOError as error:
        print("Erro: ", error)


#funcao listar produto
def listar_produto():
    try:
        arquivo = open("Dados_Produtos.txt", "r+")
        print("Lista de produto:")
        for linhas in arquivo:
            linhas = linhas.rstrip()  # funcao para tirar o enter vazio
            linhas_lista = linhas.split(" # ")
            print(linhas_lista[0],"=", linhas_lista[1], "Preço:", linhas_lista[2])
        arquivo.close()
        print("\n--------- \n")
    except IOError as error:
        print("Erro: ", error)


#funcao alterar produto
def alterar_produto(cod_p):
    try:
        with open("Dados_Produtos.txt", "r") as arquivo:
            linhas = arquivo.readlines(cod_p)
            for elemento in linhas:
                if elemento.startswith(cod_p):
                    print("Alterar Produto: ")
                    nome_p = input("Nome: ").title()
                    cod_p = input("Código: ").title()
                    preco_p = input("Preço: ")
                    quant_p = input("Quantidade:")
                    item_p = (cod_p + " # " + nome_p + " # " + preco_p + " # " + quant_p +"\n")
                    pos = linhas.index(elemento)
                    linhas.pop(pos)
                    linhas.insert(item_p)
                    arquivo = open("Dados_Produtos.txt", "w")
                    arquivo.writelines(linhas)
                    arquivo.close()
                    print("Alteração realizada com sucesso! :)")
    except IOError as error:
        print("Erro: ", error)

# funcao excluir produto
def excluir_produto(cod_p):
    try:
        arquivo = open("Dados_Produtos.txt", "r")
        linhas = arquivo.readlines()
        for elemento in linhas:
            if elemento.startswith(cod_p):
                pos = linhas.index(elemento)
                linhas.pop(pos)
                arquivo = open("Dados_Produtos.txt", "w")
                arquivo.writelines(linhas)
        arquivo.close()
        print("Produto removido! \n")
        return 0
    except IOError as error:
        print("ERRO: ", error)


#funcao copia produtos
def copia_produto():
    try:
        arquivo1 = open("Dados_Produtos.txt", "r")
        arquivo2 = open("copia_Dados_Produtos.txt", "a")
        for texto in arquivo1:
            arquivo2.write(texto)
        print("Arquivo dados produto copiado com sucesso!")
        arquivo1.close()
        arquivo2.close()
    except IOError as error:
        print("ERRO: ", error)

