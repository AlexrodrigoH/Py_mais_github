def carrinho_de_compras():
    carrinho = []
    continuar = "s"
    while continuar == "s":
        if continuar == "s":
            nome_do_produto = input("Digite o nome do produto: ")
            preco = float(input("Digite o preco do produto: R$"))
            produto = {"nome": nome_do_produto,
                        "preco": preco}
            carrinho.append(produto)
        else:
            print("Finalizando a adicao de produtos ao carrinho.")

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