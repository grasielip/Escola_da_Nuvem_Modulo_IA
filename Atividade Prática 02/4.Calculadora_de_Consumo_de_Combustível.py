# Dados da viagem
distancia = 300  # quilômetros
combustivel = 25  # litros

# Cálculo do consumo médio (km/l)
consumo_medio = distancia / combustivel

# Exibição dos dados e resultado
print(" ==== Dados da Viagem ===\n",
"Distância percorrida:", distancia, "km\n",
"Combustível gasto:", combustivel, "litros\n",
"Consumo médio:", round(consumo_medio, 2), "km/l\n",
"==============================")