#calcule a gorjeta
# --- Programa principal (versão Brasil) ---
print("Calcilo gorjeta de Gorjeta Brasil","\n-----------------------------------------")

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta com base no valor total da conta e na porcentagem desejada.

    Parâmetros:
        valor_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

    Retorna:
        float: O valor da gorjeta calculada.
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Entrada dos dados (aceita vírgulas)
valor_conta_str = input("Digite o valor total da conta (ex: 125,50): R$")
porcentagem_str = input("Digite a porcentagem da gorjeta (ex: 10): ")

# Substitui vírgula por ponto e converte para float
valor_conta = float(valor_conta_str.replace(",", "."))
porcentagem_gorjeta = float(porcentagem_str.replace(",", "."))

# Calcula a gorjeta
gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
total = valor_conta + gorjeta

# Exibe os resultados no formato brasileiro
print("\n🧾 Resultado:")
print(f"Valor da conta: R${valor_conta:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"Gorjeta ({porcentagem_gorjeta:.0f}%): R${gorjeta:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"Total a pagar: R${total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print("Final do cáculo")