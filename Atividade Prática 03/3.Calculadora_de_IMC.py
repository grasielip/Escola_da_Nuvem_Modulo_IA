print("-------------------------------------------------------\n",
      "               Calculadora de IMC\n",
      "-------------------------------------------------------\n",
      "Digite seu peso (em kg) e altura (em metros) para calcular o IMC.",)
# Função para calcular o IMC
import sys

def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura * altura)

def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obeso"

try:
    peso = float(input("Peso (kg): ").strip().replace(",", "."))
    altura = float(input("Altura (m): ").strip().replace(",", "."))
except ValueError:
    print("Entrada inválida. Use números (ex.: 70.5 ou 1.75).")
    sys.exit(1)

if altura <= 0 or peso <= 0:
    print("Peso e altura devem ser maiores que zero.")
    sys.exit(1)

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")

print("\nCálculo do IMC realizado com sucesso.",
      "\n-------------------------------------------------------")


