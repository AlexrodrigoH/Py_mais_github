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
    return carrinho