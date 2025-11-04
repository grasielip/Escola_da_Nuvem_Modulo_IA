print("CALCULO DE COMISSÃO", 
      "--------------------------------", sep="\n")
# Lê os dados de entrada
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas do mês: "))

# Calcula a comissão (15% sobre as vendas)
comissao = total_vendas * 0.15

# Calcula o total a receber
total_a_receber = salario_fixo + comissao

# Exibe o resultado formatado com duas casas decimais
print(f"TOTAL = R$ {total_a_receber:.2f}")

print("\nFIM DO PROGRAMA")
