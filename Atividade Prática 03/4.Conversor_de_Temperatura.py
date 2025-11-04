#!/usr/bin/env python3
# Conversor de temperaturas: Celsius, Fahrenheit, Kelvin
# Salve como: 4.Conversor_de_Temperatura.py
print(" Conversor de Temperatura\n",
      "--------------------------------------")

def normalize_unit(u: str) -> str | None:
    if not u:
        return None
    s = u.strip().lower().replace('°', '').replace('º', '')
    s = s.replace('celsius', 'c').replace('celcius', 'c')
    s = s.replace('fahrenheit', 'f')
    s = s.replace('kelvin', 'k')
    s = s.replace('degc', 'c').replace('degf', 'f')
    if s in ('c', 'celsius'):
        return 'C'
    if s in ('f', 'fahrenheit'):
        return 'F'
    if s in ('k', 'kelvin'):
        return 'K'
    return None

def to_celsius(value: float, unit: str) -> float:
    if unit == 'C':
        return value
    if unit == 'F':
        return (value - 32.0) * 5.0 / 9.0
    if unit == 'K':
        return value - 273.15
    raise ValueError('Unidade desconhecida')

def from_celsius(c: float, target_unit: str) -> float:
    if target_unit == 'C':
        return c
    if target_unit == 'F':
        return c * 9.0 / 5.0 + 32.0
    if target_unit == 'K':
        return c + 273.15
    raise ValueError('Unidade desconhecida')

def parse_number(s: str) -> float | None:
    if s is None:
        return None
    s = s.strip().replace(',', '.')
    try:
        return float(s)
    except ValueError:
        return None

def main():
    print("Conversor de temperatura (Celsius, Fahrenheit, Kelvin)")
    temp_input = input("Informe a temperatura (ex: 36.6): ").strip()
    temp = parse_number(temp_input)
    if temp is None:
        print("Valor de temperatura inválido.")
        return

    src = normalize_unit(input("Unidade de origem (C, F, K): "))
    if src is None:
        print("Unidade de origem inválida. Use C, F ou K.")
        return

    dst = normalize_unit(input("Unidade destino (C, F, K): "))
    if dst is None:
        print("Unidade destino inválida. Use C, F ou K.")
        return

    if src == 'K' and temp < 0:
        print("Temperatura em Kelvin não pode ser negativa.")
        return

    if src == dst:
        unit_symbols = {'C': '°C', 'F': '°F', 'K': 'K'}
        print(f"{temp:.2f} {unit_symbols[src]} (sem alteração)")
        return

    c = to_celsius(temp, src)
    result = from_celsius(c, dst)

    # detectar resultado fisicamente inválido em Kelvin
    if dst == 'K' and result < 0:
        print("Aviso: resultado abaixo de 0 K (fisicamente inválido).")

    symbols = {'C': '°C', 'F': '°F', 'K': 'K'}
    print(f"{temp:.2f} {symbols[src]} = {result:.2f} {symbols[dst]}")

if __name__ == "__main__":
    main()

    print("\nPrograma encerrado.")