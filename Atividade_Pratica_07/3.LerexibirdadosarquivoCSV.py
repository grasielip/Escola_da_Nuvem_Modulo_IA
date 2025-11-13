import csv

with open("pessoas.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    print("Dados do arquivo CSV:")
    for linha in leitor:
        print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")
