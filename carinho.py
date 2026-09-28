import armazena_dados
import msvcrt
import subprocess

def carrinho_de_compras():
    carrinho = []
    estoque = []
    while True:
        estoque.clear()
        separado = armazena_dados.ler_dados().split("\n")
        for produto_s in separado:
            if produto_s == "":
                continue
            produto_separado = produto_s.split(";")
            preco = float(produto_separado[1])
            nome = produto_separado[0]
            estoque.append({"nome": nome, "preco": preco})
        try:
            while True:
                print("============ MENU ============")
                escolha = input("1- Adicionar produto ao estoque \n2- Ver produtos em estoque \n3- Adicionar ao carrinho\n4- apagar produtos \n5- sair ")
                if not escolha.isdigit():
                    print("Somente numeros e permitido!\n")
                    continue
                escolha = int(escolha)
                if escolha <= 0 or escolha > 5:
                    print("Escolha somente as opcoes 1, 2.... do menu!\n")
                    continue
                break
            #======ADICIONA PRODUTOS AO ESTOQUE======
            if escolha == 1:
                while True:
                    print("PARA SAIR NAO INFORME NENHUM PRODUTO (PRECIONE ENTER)\n")
                    nome_produto = input("Digite o nome do produto: ").strip().lower()
                    nome_produto = " ".join(nome_produto.split())
                    repetido = False
                    for produto in estoque:
                        if produto['nome'] == nome_produto:
                            print("Produto ja exite no estoque.\n")
                            repetido = True
                            break
                    if repetido == True: continue
                    encerrar = False
                    if nome_produto == "":
                        sair = input("Deseja realmente sair do estoque? (s/n): ").lower().strip()
                        while sair != "s" and sair != "n":
                            print("Opcao invalida. Digite 's' para sim ou 'n' para nao.")
                            sair = input("Deseja realmente sair do estoque? (s/n): ").lower().strip()
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
                    continue
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
                estoque.append({"nome": nome_produto, "preco": preco_produto})
                armazena_dados.armazenar_produtos(nome_produto, preco_produto)
                subprocess.run("cls", shell=True)
                print(f"Produto '{nome_produto}' adicionado ao carrinho com sucesso!\n")
            #======VER OS PRODUTOS DA LISTA======
            elif escolha == 2:
                lista = 1
                print("\n=== PRODUTOS EM ESTOQUE ===")
                for produto in estoque:
                    print(f"{lista} - Produto: {produto['nome']}, Preco: R${produto['preco']:.2f}")
                    lista += 1
                print("\n")
            #======ADICIONAR PRODUTOS AO CARRINHO======
            elif escolha == 3:
                while True:
                    print("Informe o NUMERO do produto que deseja adicionar: \n")
                    print("Para sair precione 'ESC'!\n")
                    tecla = msvcrt.getch()
                    if tecla == b"\x1b":
                        if not carrinho:
                            break
                        else:
                            print("Exibindo produtos: \n")
                            for produto in estoque:
                                print("Codigo   ")
                                print(f"{lista} - produto: {produto['nome']}: R${produto['preco']:.2f}\n")
                                lista+= 1
                        break
                    else:
                        opcao = tecla.decode()
                        if not opcao.isdigit():
                            subprocess.run("cls", shell=True)
                            print("informe somente produtos correspondentes a numeros da lista!\n")
                            continue
                        opcao = int(opcao)
                        if opcao > len(estoque) or opcao <= 0:
                            print("Nosso estoque posssui ", len(estoque), " produtos!\n")
                            continue
                        else:
                            carrinho.append(estoque[opcao-1])
                            subprocess.run("cls", shell=True)
                            print("\n-->> Produto adicionado com sucesso!!\n")                   
            #Apagar produtos determinado
            elif escolha == 4:
                estoque_temp = []
                excluir = input("Informe o codigo do produto para excluir: ").strip().lower()
                for produto in estoque:
                    if produto == estoque[int(excluir)-1]:
                        continue
                    else:
                        estoque_temp.append(produto)
                armazena_dados.apagar_produto(estoque_temp)
            elif escolha == 5:
                subprocess.run("cls", shell=True)
                print(">>>> ENCERRANDO <<<<")
                lista = 1
                total_da_compra = 0
                for produto in carrinho:
                    lista+= 1
                    total_da_compra += produto["preco"]
                return total_da_compra
        except ValueError:
                print("Preco invalido. Digite um valor numerico.\n")