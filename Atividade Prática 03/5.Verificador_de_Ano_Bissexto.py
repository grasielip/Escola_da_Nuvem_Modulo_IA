print("-------------------------------",
       "Verificador de Ano Bissexto",
      "-------------------------------",sep="\n")

def is_leap_year(year):
    # Check if year is divisible by 4
    if year % 4 == 0:
        # If year is century (divisible by 100)
        if year % 100 == 0:
            # Check if it's divisible by 400
            return year % 400 == 0
        return True
    return False

# Get input from user
year = int(input("Digite um ano para verificar se é bissexto: "))

# Check if it's leap year and print result
if is_leap_year(year):
    print(f"{year} é um ano bissexto!\n",
               "Fim do programa.\n"
          "---------------------------")
else:
    print(f"{year} não é um ano bissexto\n!",
                "Fim do programa.\n",
          "---------------------------")

    print()