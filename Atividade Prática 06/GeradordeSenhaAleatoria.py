import random
import string

print("Programa: Gerador de Senha Aleatória\n")

# Entrada do usuário
tamanho = int(input("Digite a quantidade de caracteres da senha: "))

# Caracteres: letras, números e símbolos
caracteres = string.ascii_letters + string.digits + string.punctuation

# Gera a senha
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

print(f"\nSua senha aleatória é: {senha}")
input("\nPressione Enter para sair...")