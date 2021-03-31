def menu_venda():
    print("GERENCIADOR DE VENDAS \n"
          "1 - Registrar venda \n"
          "2 - Buscar venda \n"
          "3 - Listar vendas \n"
          "4 - Excluir venda \n"
          "5 - Comprar produto \n"
          "6 - "
          "Digite a opção: ")
    return input()

#funcao pesquisar vendedor
print("Selecione um vendedor:")
arquivo = open("Dados_Funcionários.txt", "r+")
contador= 0
for linha in arquivo:
    linha = linha.rstrip()
    if codigo_func in linha:
        contador +=1
        print(linha)
    else:
        print("Vendedor não encontrado!")
        return input()
    arquivo.close()


#funcao pesquisar cliente
def buscar_cliente(cpf_c):
    try:
        arquivo = open("Dados_Clientes.txt", "r+")
        contador= 0
        for linha in arquivo:
            linha = linha.rstrip()
            if cpf_c in linha:
                contador +=1
                print(linha)
            else:
                print("Cliente não encontrado!")
                return cadastro_cliente()
        arquivo.close()
    except IOError as error:
        print("Erro: ", error)

