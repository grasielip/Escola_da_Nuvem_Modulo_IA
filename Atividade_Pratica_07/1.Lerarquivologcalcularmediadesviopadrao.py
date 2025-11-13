import os
from statistics import mean, stdev

arquivo_log = "log_treinamento.txt"

# Cria o arquivo se não existir
if not os.path.exists(arquivo_log):
    with open(arquivo_log, "w", encoding="utf-8") as f:
        f.write("Treinamento 1: 12.4\nTreinamento 2: 11.9\nTreinamento 3: 13.2\nTreinamento 4: 12.8\n")

tempos = []

# Lê o arquivo e extrai os tempos numéricos
with open(arquivo_log, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        partes = linha.strip().split(":")
        if len(partes) == 2:
            try:
                tempos.append(float(partes[1]))
            except ValueError:
                pass

# Calcula média e desvio padrão
if tempos:
    print(f"Média: {mean(tempos):.2f}")
    print(f"Desvio padrão: {stdev(tempos):.2f}")
else:
    print("Nenhum valor válido encontrado.")
