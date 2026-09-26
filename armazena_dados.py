def armazenar_produtos(nome_produto, preco_produto):
    arquivo = open("produtos.txt", "a") 
    arquivo.write(f"{nome_produto};{preco_produto}\n")
    arquivo.close()
def ler_dados():
    arquivo = open("produtos.txt", "r")
    ler_arquivo = arquivo.read()
    arquivo.close()
    return ler_arquivo