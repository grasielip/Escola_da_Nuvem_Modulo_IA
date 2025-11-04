print("Calculadora de Desconto")
print("-----------------------")
# Variaveis
Nome_produto = "Camiseta"
Preço_original = 50.00
Porcentagem_desconto = 20
# Calculo do desconto
Valor_desconto = (Porcentagem_desconto / 100) * Preço_original
Preço_final = Preço_original - Valor_desconto
# Mostrar na tela
print(f"""Produto: {Nome_produto}
Preço Original: R$ {Preço_original:.2f}
Desconto: {Porcentagem_desconto}%
Preço Final: R$ {Preço_final:.2f}
-----------------------
Desconto aplicado com sucesso!""")