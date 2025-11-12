import requests

print("Programa: Consulta de Endereço por CEP\n")

cep = input("Digite o CEP (somente números): ").strip()

url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    if "erro" not in dados:
        print(f"\nLogradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
    else:
        print("CEP não encontrado.")
else:
    print("Erro na consulta. Verifique o CEP e tente novamente.")
input("\nPressione Enter para sair...")