import csv

dados = [
    {"Nome": "Grasieli", "Idade": 28, "Cidade": "Volta Redonda"},
    {"Nome": "Carlos", "Idade": 30, "Cidade": "São Paulo"},
    {"Nome": "Ana", "Idade": 25, "Cidade": "Rio de Janeiro"}
]

with open("pessoas.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    colunas = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerows(dados)

print("Arquivo CSV criado com sucesso!")
