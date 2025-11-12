import requests

print("Programa: Consulta de Cotação de Moeda\n")

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    chave = f"{moeda}BRL"

    if chave in dados:
        info = dados[chave]
        print(f"\nMoeda: {moeda}/BRL")
        print(f"Valor atual: R${float(info['bid']):.2f}")
        print(f"Máximo do dia: R${float(info['high']):.2f}")
        print(f"Mínimo do dia: R${float(info['low']):.2f}")
        print(f"Última atualização: {info['create_date']}")
    else:
        print("Moeda não encontrada.")
else:
    print("Erro ao consultar cotação. Verifique o código da moeda.")
input("\nPressione Enter para sair...")