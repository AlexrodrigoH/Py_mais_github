#from os import replace

def carrinho_de_compras():
    carrinho = []
    continuar = "s"
    while continuar == "s":
        if continuar == "s":
           while True:
                try:
                    flagS = True
                    nome_produto = input("Digite o nome do produto: ").strip()
                    preco_produto = input("Digite o preco do produto: ").strip()
                    if nome_produto == "" and preco_produto != "":
                        print("Nome do produto invalido. Digite um nome valido.\n")
                        continue
                    elif preco_produto == "" and nome_produto != "":
                        print("Preco do produto invalido. Digite um preco valido.\n")
                        continue
                    elif preco_produto == "" and nome_produto == "":
                        break
                    preco_produto = preco_produto.replace(",", ".")
                    for caractere in preco_produto:
                        if caractere in "0123456789.": #verifica se o preco do produto e valido
                            continue
                        else:
                            print("\nDigite somente valor numerico para o PRECO (0123456789) separado por ponto (.)!\n")
                            flagS = False
                            break
                    if flagS == False:
                        continue
                    preco_produto = float(preco_produto)
                    if preco_produto <= 0:
                        print("Preco invalido. Digite um valor positivo maior que zero.\n")
                        continue
                    carrinho.append({"nome": nome_produto, "preco": preco_produto})
                    print(f"Produto '{nome_produto}' adicionado ao carrinho com sucesso!\n")
                    break
                except ValueError:
                    print("Preco invalido. Digite um valor numerico.\n")
        else:
            print("Finalizando a adicao de produtos ao carrinho.")
        if not carrinho:
            return None
        continuar = input("Deseja adicionar produto(os)? (s/n): ").lower()
        while continuar != "s" and continuar != "n":
            print("Opcao invalida. Digite 's' para sim ou 'n' para nao.")
            continuar = input("Deseja adicionar produto(os)? (s/n): ").lower()
    total_da_compra = 0
    exibir = input("Deseja exibir lista do carrinho de compras? (s/n): ").lower()
    lista = 1
    for produto in carrinho:
                total_da_compra += produto['preco']
    if exibir == "s":
        print("\n=== CARRINHO DE COMPRAS ===")
        for produto in carrinho:
            print(f"{lista} - Produto: {produto['nome']}, Preco: R${produto['preco']:.2f}")
            lista += 1
    else:
        print("Lista do carrinho de compras nao exibida.\n")
    return total_da_compra