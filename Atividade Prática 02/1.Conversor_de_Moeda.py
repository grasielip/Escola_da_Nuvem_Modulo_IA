print("Conversor de Moeda - BRL para USD e EUR")
print("---------------------------------------")

# Variaveis
Valoremreais = 100.00
Taxa_dolar = 5.60   # 1 USD = 5.60 BRL
Taxa_euro = 6.60    # 1 EUR = 6.60 BRL

# Calculo da conversao

valor_dolar = Valoremreais / Taxa_dolar
valor_euro = Valoremreais / Taxa_euro

# Mostrar na tela

print(f"Dolar US$: {valor_dolar:.2f}\nEuro €: {valor_euro:.2f}","\nConversão concluída com sucesso!")

print("----------------------------------------")



