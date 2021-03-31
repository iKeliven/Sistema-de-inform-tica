
"""
#importando arquivos das funcoes
from funcao_funcionario import*
from funcao_cliente import*
from funcao_produto import*

#chamando vendedor
cod_f=input("Digite o codigo do vendedor: ").title()

#importando função buscar vendedor
buscar_funcionario(cod_f)

#pedindo cpf do cliente
cpf_c = input("Digite o CPF do cliente: ")

#importando função buscar cliente
buscar_cliente(cpf_c)
"""

#área de venda
print('Digite o código do produto ou 0 para parar!')
#funcao buscar produto
while True:
    cod_p = input("Produto: ").title()
    if cod_p == 0:
        break
    else:
        arquivo = open("Dados_Produtos.txt", "r")
        for linha in arquivo:
            contador = 0
            lista_p = []
            if cod_p in linha:
                linha_lista = linha.split(" # ")
                # transformando em float
                float_p = float(linha_lista[2].replace(',', '.'))
                lista_p.append(float_p)
                print(linha_lista[0], "=", linha_lista[1], " Preço:", float_p)
                #inserindo valores na lista
            else:
                break
total = sum(lista_p)
print("Total: ", total)



