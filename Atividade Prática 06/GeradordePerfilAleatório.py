import requests

print("Programa: Gerador de Perfil de Usuário Aleatório\n")

url = "https://randomuser.me/api/"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    usuario = dados['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")
else:
    print("Erro ao gerar usuário. Tente novamente.")
input("\nPressione Enter para sair...")
