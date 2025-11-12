from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade aproximada de uma pessoa em dias com base no ano de nascimento.

    Parâmetro:
        ano_nascimento (int): O ano de nascimento da pessoa.

    Retorna:
        int: A idade aproximada em dias.
    """
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # aproximação, sem considerar anos bissextos
    return idade_dias


# --- Programa principal ---
print("Programa: Cálculo da Idade em Dias\n")

ano = int(input("Digite o ano de nascimento: "))
idade_dias = calcular_idade_em_dias(ano)

print(f"\nSua idade aproximada em dias é: {idade_dias} dias.")
