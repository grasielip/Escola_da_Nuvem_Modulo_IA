import string

def verificar_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo.
    Ignora espaços, acentuação e pontuação.

    Parâmetro:
        texto (str): Palavra ou frase a ser verificada.

    Retorna:
        str: "Sim" se for palíndromo, "Não" caso contrário.
    """
    # Deixa tudo minúsculo e remove espaços e pontuação
    texto_limpo = ''.join(
        c.lower() for c in texto if c.isalnum()
    )

    # Verifica se é igual ao reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


# --- Programa principal ---
print("🔎 Verificador de Palíndromos\n")

frase = input("Digite uma palavra ou frase: ")
resultado = verificar_palindromo(frase)

print(f"\nÉ palíndromo? {resultado}")
