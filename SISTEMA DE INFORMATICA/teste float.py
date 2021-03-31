cod_p=input("Digite o codigo: ") .title()

arquivo = open("Dados_Produtos.txt", "r")
for linha in arquivo:
    if cod_p in linha:
        linha_lista = linha.split(" # ")
        print(linha_lista[2])
        prod = float(linha_lista[2].replace(',', '.'))
        print(prod+prod)



