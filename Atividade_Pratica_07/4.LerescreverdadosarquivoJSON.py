import json

# Dados de exemplo
pessoa = {
    "nome": "Grasieli",
    "idade": 28,
    "cidade": "Volta Redonda"
}

# Escrever em JSON
with open("pessoa.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(pessoa, arquivo_json, ensure_ascii=False, indent=4)
print("Arquivo JSON criado com sucesso!")

# Ler do JSON
with open("pessoa.json", "r", encoding="utf-8") as arquivo_json:
    dados = json.load(arquivo_json)
    print("Dados lidos do JSON:")
    print(f"Nome: {dados['nome']}, Idade: {dados['idade']}, Cidade: {dados['cidade']}")
