# Area da circunferência
# https://www.beecrowd.com.br/judge/pt/problems/view/1002

print(" -------------------------------------------------------\n",
      "               Área da circunferência\n",
        "-------------------------------------------------------\n",
        "Digite o raio da circunferência para calcular a área.",)

PI = 3.14159265

# Ler o raio da circunferência

raio = float(input(" Raio:"))

# CaLculo da área
area = PI * (raio ** 2)

# Mostrar o resultado com 4 casas decimais
print(f" A={area:.4f}\n",
      "-------------------------------------------------------\n",
      "Final do programa.")
