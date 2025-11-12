def calcular_preco_final(preco_original: float, percentual_desconto: float) -> float:
    """
    Calcula o preço final de um produto após aplicar o desconto.

    Parâmetros:
        preco_original (float): O preço original do produto.
        percentual_desconto (float): O percentual de desconto (ex: 10 para 10%).

    Retorna:
        float: O preço final após o desconto.
    """
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return preco_final


# --- Programa principal ---
print("Calculadora de Desconto\n")

# Entrada de dados
preco_str = input("Digite o preço original do produto (ex: 250,75): R$")
desconto_str = input("Digite o percentual de desconto (ex: 10): ")

# Conversão para float, aceitando vírgula
preco_original = float(preco_str.replace(",", "."))
percentual_desconto = float(desconto_str.replace(",", "."))

# Cálculo
preco_final = calcular_preco_final(preco_original, percentual_desconto)

# Exibição formatada (padrão brasileiro)
print("\n Resultado:")
print(f"Preço original: R${preco_original:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"Desconto: {percentual_desconto:.0f}%")
print(f"Preço final: R${preco_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
