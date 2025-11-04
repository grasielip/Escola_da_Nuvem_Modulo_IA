print("Calculadora da Média", "--------------------", sep="\n")
# Leitura das notas com prompt visível
N1 = float(input("Primeira nota: "))
N2 = float(input("Segunda nota: "))
N3 = float(input("Terceira nota: "))
N4 = float(input("Quarta nota: "))

# Cálculo da média com pesos
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

# Exibição da média
print(f"Media: {media:.1f}")

# Verificação da situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input("Nota do exame: "))
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")
