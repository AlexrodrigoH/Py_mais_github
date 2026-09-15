import descontos

print("=== LOJA PYTHON ===")
nome = input("Digite seu nome: ")
print ("Bem vindo, ", nome)
quantidade = int(input("Quantos produto(os) deseja comprar? "))
print("Voce deseja comprar ", quantidade, " produto(os)!")
preco = float(input("Digite o preco do produto: R$ "))
print("Valor do produto e: R$", preco)
total_da_compra = quantidade * preco
print(f"\nO valor total bruto da compra e: R${total_da_compra:.2f}\n")
total_da_compra, percentual, desconto = descontos.calcular_desconto(total_da_compra)
if percentual > 0:
    print(f"Voce recebeu um desconto de {percentual:.0f}%!\n")
    print(f"Voce economizou: R${desconto:.2f}\n")
    print(f"O valor total liquido da compra e: R${total_da_compra:.2f}\n")
else:
    print("Nenhum desconto aplicado.\n")
    print(f"O valor total liquido da compra e: R${total_da_compra:.2f}\n")
print( "\nObrigado por visitar nossa loja!" )