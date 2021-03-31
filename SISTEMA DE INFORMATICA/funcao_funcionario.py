#funcao menu do funcionário
def menu_funcionario():
    print("Escolha a opção: \n"
          "1 - Cadastrar Funcionário \n"
          "2 - Pesquisar Funcionário \n"
          "3 - Listar Funcionários \n"
          "4 - Alterar Funcionário \n"
          "5 - Excluir Funcionário \n"
          "6 - Fazer uma Cópia ")
    return input()

#funcao validação do menu do funcionario
def validar_menu_funcionario():
    while True:
        opcao = menu_funcionario()
        if opcao == "1":
            cadastro_funcionario()
        elif opcao == "2":
            cpf_f = input("Digite o CPF do funcionário: ")
            buscar_funcionario(cpf_f)
        elif opcao == "3":
            listar_funcionario()
        elif opcao == "4":
            cpf_f = input("Digite o CPF do funcionário: ")
            alterar_funcionario(cpf_f)
        elif opcao == "5":
            cpf_f = input("Digite o CPF do funcionário: ")
            excluir_funcionario(cpf_f)
        elif opcao == "6":
            copia_funcionario()
        else:
            print ("Programa Finalizado!")
            break


#funcao cadastro cliente
def cadastro_funcionario():
    try:
        arquivo = open("Dados_Funcionarios.txt", "a")
        print("Cadastrar Funcionário: ")
        nome_f = input("Nome completo: ").title()
        nascimento_f = input("Data de Nascimento: ")
        cpf_f = input("CPF: ")
        telefone_f = input("Telefone: ")
        endereco_f = input("Endereço: ")
        salario_f = input("Salário:")
        cargo_f = input("Cargo: ")
        contratacao_f = input("Data de contratação: ")
        arquivo.write(nome_f + " # " + nascimento_f + " # " + cpf_f + " # " + telefone_f + " # " + endereco_f +
                      " # " + salario_f + " # " + cargo_f + " # " + contratacao_f + "\n")
        arquivo.close()
        print("Funcionário cadastrado com sucesso!")
    except IOError as error:
        print("Erro: ", error)

#funcao pesquisar funcionario
def buscar_funcionario(cpf_c):
    try:
        arquivo = open("Dados_Funcionarios.txt", "r+")
        contador= 0
        for linha in arquivo:
            linha = linha.rstrip()
            if cpf_c in linha:
                contador +=1
                print(linha)
            else:
                print("Funcionario não encontrado!")
                cadastro_funcionario()
        arquivo.close()
    except IOError as error:
        print("Erro: ", error)


#funcao listar funcionario
def listar_funcionario():
    try:
        arquivo = open("Dados_Funcionarios.txt", "r+")
        print("Lista de funcionários: \n")
        for linhas in arquivo:
            print(linhas)
        arquivo.close()
    except IOError as error:
        print("Erro: ", error)


#funcao alterar funcionario
def alterar_funcionario(cpf_f):
    try:
        with open("Dados_Funcionarios.txt", "r") as arquivo:
            linhas = arquivo.readlines(cpf_f)
            for elemento in linhas:
                if elemento.startswith(cpf_f):
                    print("Alterar Funcionario: ")
                    nome_f = input("Nome completo: ").title()
                    nascimento_f = input("Data de Nascimento: ")
                    cpf_f = input("CPF: ")
                    telefone_f = input("Telefone: ")
                    endereco_f = input("Endereço: ")
                    salario_f = input("Salário:")
                    cargo_f = input("Cargo: ")
                    contratacao_f = input("Data de contratação: ")
                    item_f = (nome_f + " # " + nascimento_f + " # " + cpf_f + " # " + telefone_f + " # " + endereco_f +
                              " # " + salario_f + " # " + cargo_f + " # " + contratacao_f + "\n")
                    pos = linhas.index(elemento)
                    linhas.pop(pos)
                    linhas.insert(item_f)
                    arquivo = open("Dados_Funcionarios.txt", "w")
                    arquivo.writelines(linhas)
                    arquivo.close()
                    print("Alteração realizada com sucesso! :)")
    except IOError as error:
        print("Erro: ", error)

# funcao excluir funcionario
def excluir_funcionario(cpf_f):
    try:
        arquivo = open("Dados_Funcionários.txt", "r")
        linhas = arquivo.readlines()
        for elemento in linhas:
            if elemento.startswith(cpf_f):
                pos = linhas.index(elemento)
                linhas.pop(pos)
                arquivo = open("Dados_Funcionarios.txt", "w")
                arquivo.writelines(linhas)
        arquivo.close()
        print("Funcionário removido! \n")
        return 0
    except IOError as error:
        print("ERRO: ", error)


#funcao copia funcionario
def copia_funcionario():
    try:
        arquivo1 = open("Dados_Funcionarios.txt", "r")
        arquivo2 = open("copia_Dados_Funcionários.txt", "a")
        for texto in arquivo1:
            arquivo2.write(texto)
        print("Arquivo dados funcionário copiado com sucesso!")
        arquivo1.close()
        arquivo2.close()
    except IOError as error:
        print("ERRO: ", error)
