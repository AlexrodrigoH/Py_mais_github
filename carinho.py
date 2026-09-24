import armazena_dados

def carrinho_de_compras():
    carrinho = []
    novo_produto = []
    continuar = "s"
    while continuar == "s":
        while True:
            try:
                while True:
                    print("============ MENU ============")
                    escolha = int(input("1- Adicionar produto ao estoque \n2- Ver produtos \n3- Adicionar ao carrinho \n4- sair "))
                    if escolha != 1 and escolha != 2 and escolha != 3:
                        print("Escolha somente as opcoes 1, 2 ou 3 do menu!")
                        continue
                    break
                #======ADICIONA PRODUTOS AO ESTOQUE======
                if escolha == 1:
                    while True:
                        nome_produto = input("Digite o nome do produto: ").strip()
                        nome_produto = " ".join(nome_produto.split())
                        repetido = False
                        for produto in carrinho:
                            if produto['nome'].lower() == nome_produto.lower():
                                print("Produto ja exite no carrinho.\n")
                                repetido = True
                                break
                        if repetido:
                            continue
                        encerrar = False
                        if nome_produto == "":
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
                        break
                    if encerrar:
                        break
                    while True:
                        preco_produto = input("Digite o preco do produto: ").strip()
                        preco_produto = preco_produto.replace(" ", "")
                        preco_produto = preco_produto.replace(",", ".")
                        if preco_produto == "":
                            print("Preco do produto invalido. Digite um preco valido.\n")
                            continue
                        caracteres_validos = True
                        for caractere in preco_produto:
                            if caractere in "0123456789.": #verifica se o preco do produto e valido
                                continue
                            else:
                                caracteres_validos = False  
                                break
                        try:
                            preco_produto = float(preco_produto)
                        except ValueError:
                            print("Preco invalido. Digite um valor valido (EX: 12.99)!\n")
                            continue
                        if caracteres_validos == False:
                            print("\nDigite somente valor numerico para o PRECO (0123456789) separado por ponto (.)!\n")
                            continue
                        break
                    if preco_produto <= 0:
                        print("Preco invalido. Digite um valor positivo maior que zero.\n")
                        continue
                    novo_produto.append({"nomeNew": nome_produto, "preco": preco_produto})
                    carrinho.append({"nome": nome_produto, "preco": preco_produto})
                    armazena_dados.armazenar_produtos(nome_produto, preco_produto)
                    print(f"Produto '{nome_produto}' adicionado ao carrinho com sucesso!\n")
                    continuar = input("Deseja adicionar produto(os)? (s/n): ").lower().strip()
                    while continuar != "s" and continuar != "n":
                        print("Opcao invalida. Digite 's' para sim ou 'n' para nao.")
                        continuar = input("\nDeseja adicionar produto(os)? (s/n): \n").lower().strip()
                    break
                #======VER OS PRODUTOS DA LISTA======
                elif escolha == 2:
                    separado = armazena_dados.ler_dados().split("\n")
                    for produto_s in separado:
                        if produto_s == "":
                                    continue
                        produto_separado = produto_s.split(";")
                        preco = float(produto_separado[1])
                        nome = produto_separado[0]
                        carrinho.append({"nome": nome, "preco": preco})
                    total_da_compra = 0
                    lista = 1
                    #for produto in carrinho:
                     #   total_da_compra += produto["preco"]
                    print("\n=== PRODUTOS EM ESTOQUE ===")
                    for produto in carrinho:
                        print(f"{lista} - Produto: {produto['nome']}, Preco: R${produto['preco']:.2f}")
                    
                        lista += 1
                    print("\n")
                    #return total_da_compra
            except ValueError:
                    print("Preco invalido. Digite um valor numerico.\n")
        if encerrar == True:
            break
