import descontos
import carinho

print("=== LOJA PYTHON ===")
total_bruto = carinho.carrinho_de_compras()
print("\n=== RESUMO DA COMPRA ===\n")
print(f"\nO valor total bruto da compra e: R${total_bruto:.2f}\n")
total_da_compra, percentual, desconto = descontos.calcular_desconto(total_bruto)
if percentual > 0:
    print(f"Voce recebeu um desconto de {percentual:.0f}%!\n")
    print(f"Voce economizou: R${desconto:.2f}\n")
    print(f"--O valor total liquido da compra e: R${total_da_compra:.2f}\n")
else:
    print("--Nenhum desconto aplicado.--\n")
    print(f"--O valor total liquido da compra e: R${total_da_compra:.2f}\n")
print( "\nObrigado por visitar nossa loja!")