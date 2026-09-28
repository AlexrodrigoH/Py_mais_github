import subprocess
def armazenar_produtos(nome_produto, preco_produto):
    arquivo = open("produtos.txt", "a") 
    arquivo.write(f"{nome_produto};{preco_produto}\n")
    arquivo.close()
def ler_dados():
    arquivo = open("produtos.txt", "r")
    ler_arquivo = arquivo.read()
    arquivo.close()
    return ler_arquivo
def apagar_produto(new_list):
    arquivo = open("produtos.txt", "w")
    for produto in new_list:
        arquivo.write(f"{produto['nome']};{produto['preco']}\n")
    subprocess.run("cls", shell=True)
    print("\n==>PRODUTO APAGADO COM SUCESSO!<==\n")
    arquivo.close()