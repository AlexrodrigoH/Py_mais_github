def calcular_desconto(total_da_compra, percentual=0):
    if total_da_compra >= 100 and total_da_compra < 200:
        percentual = 10
        desconto = total_da_compra * 0.10
        total_da_compra -= desconto
        return total_da_compra, percentual, desconto
    elif total_da_compra >= 200 and total_da_compra < 500:
        percentual = 20
        desconto = total_da_compra * 0.20
        total_da_compra -= desconto
        return total_da_compra, percentual, desconto
    elif total_da_compra >= 500:
        percentual = 35
        desconto = total_da_compra * 0.35
        total_da_compra -= desconto
        return total_da_compra, percentual, desconto
    else:
        return total_da_compra, 0, 0