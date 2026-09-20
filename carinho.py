def carrinho_de_compras():
    carrinho = []
    continuar = "s"
    while continuar == "s":
        while True:
            try:
                nome_produto = input("Digite o nome do produto: ").strip()
                preco_produto = input("Digite o preco do produto: ").strip()
                encerrar = False
                if nome_produto == "" and preco_produto != "":
                    print("Nome do produto invalido. Digite um nome valido.\n")
                    continue
                elif preco_produto == "" and nome_produto != "":
                    print("Preco do produto invalido. Digite um preco valido.\n")
                    continue
                elif preco_produto == "" and nome_produto == "":
                    sair = input("Deseja realmente sair do carrinho de compras? (s/n): ").lower().strip()
                    while sair != "s" and sair != "n":
                        print("Opcao invalida. Digite 's' para sim ou 'n' para nao.")
                        sair = input("Deseja realmente sair do carrinho de compras? (s/n): ").lower().strip()
                    if sair == "s":
                        encerrar = True
                        break
                    else:
                        continue
                letra_valida = False
                caracteres_validos = True
                for caractere in nome_produto:
                    if caractere.isalpha(): #verifica se o nome do produto e valido
                        letra_valida = True
                    elif caractere.isdigit() or caractere.isspace():
                        continue
                    else:
                        caracteres_validos = False
                        break
                if letra_valida == False or caracteres_validos == False:
                    print("\nDigite somente letras, numeros e espacos para o NOME do produto!\n")
                    continue
                preco_produto = preco_produto.replace(",", ".")
                caracteres_validos = True
                for caractere in preco_produto:
                    if caractere in "0123456789.": #verifica se o preco do produto e valido
                        continue
                    else:
                        print("\nDigite somente valor numerico para o PRECO (0123456789) separado por ponto (.)!\n")
                        caracteres_validos = False
                        break
                if caracteres_validos == False:
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
        if encerrar == True:
            break
        continuar = input("Deseja adicionar produto(os)? (s/n): ").lower().strip()
        while continuar != "s" and continuar != "n":
            print("Opcao invalida. Digite 's' para sim ou 'n' para nao.")
            continuar = input("\nDeseja adicionar produto(os)? (s/n): \n").lower().strip()
    if not carrinho:
        return None
    total_da_compra = 0
    exibir = input("\nDeseja exibir lista do carrinho de compras? (s/n): \n").lower().strip()
    while exibir != "s" and exibir != "n":
                print("Opcao invalida. Digite 's' para sim ou 'n' para nao.")
                exibir = input("\nDeseja exibir lista do carrinho de compras? (s/n): \n").lower().strip()
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