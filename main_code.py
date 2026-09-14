print("=== LOJA PYTHON ===")
nome = input("Digite seu nome: ")
print ("Bem vindo, ", nome)
quantidade = int(input("Quantos produto(os) deseja comprar? "))
print("Voce deseja comprar ", quantidade, " produto(os)!")
preco = float(input("Digite o preco do produto: "))
print("Valor do produto e: R$", preco)
total_da_compra = quantidade * preco
print(f"O valor total da compra e: R${total_da_compra:.2f}\n")
tem_desconto = total_da_compra >= 100
if tem_desconto:
    print("Voce ganhou um desconto de 10%!")
    desconto = total_da_compra * 0.10
    total_da_compra -= desconto
    print(f"Valor total a pagar com desconto: R${total_da_compra:.2f}")
else:
    print("Nenhum desconto disponivel para compras abaixo de R$100,00!")
    print(f"Valor total a pagar: R${total_da_compra:.2f}")
print("\nObrigado por visitar nossa loja!")