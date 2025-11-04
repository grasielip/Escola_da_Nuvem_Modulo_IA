# Lê os dados do funcionário
numero_funcionario = int(input("Digite o número do funcionário: ").strip())
horas_trabalhadas = int(input("Digite as horas trabalhadas: ").strip().replace(',', '.'))
valor_por_hora = float(input("Digite o valor por hora: ").strip().replace(',', '.'))

# Calcula o salário
salario = horas_trabalhadas * valor_por_hora

# Exibe o resultado 
print("Calculadora de salário por horas trabalhadas",
"\n---------------------------")
print(f"Número do Funcionário = {numero_funcionario}")
print(f"Salário = R$ {salario:.2f}")
print("---------------------------", "\nFim do Programa")