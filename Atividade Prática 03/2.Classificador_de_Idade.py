import sys

#!/usr/bin/env python3
# /workspaces/Escola_da_Nuvem_Modulo_IA/Atividade Prática 03/2.Classificador_de_Idade.py

print(" -------------------------------------------------------\n",
      "               Classificador de Idade\n",
      "-------------------------------------------------------\n",
      "Digite sua idade para saber a classificação correspondente.",)


def classificar_idade(idade: int) -> str:
    if idade < 0:
        raise ValueError(" Idade não pode ser negativa.")
    if idade <= 12:
        return "Criança (0-12 anos)"
    if 13 <= idade <= 17:
        return "Adolescente (13-17 anos)"
    if 18 <= idade <= 59:
        return "Adulto (18-59 anos)"
    return "Idoso (60 anos ou mais)"

def main():
    try:
        entrada = input(" Digite sua idade: ").strip()
        idade = int(entrada)
    except ValueError:
        print("Entrada inválida. Informe um número inteiro não negativo para a idade.")
        sys.exit(1)

    try:
        categoria = classificar_idade(idade)
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)

    print(f"Classificação: {categoria}")

if __name__ == "__main__":
    main()

print("-------------------------------------------------------\n",
      "Final do programa.")