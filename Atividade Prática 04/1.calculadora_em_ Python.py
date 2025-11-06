print("calculadora \n", "----------------------------------")
def calculadora():
    while True:
        try:
            # Solicita o primeiro número
            num1 = float(input("Digite o primeiro número: "))
            
            # Solicita o segundo número
            num2 = float(input("Digite o segundo número: "))
            
            # Solicita a operação
            operacao = input("Digite a operação (+, -, *, /): ").strip()
            
            # Verifica se a operação é válida
            if operacao not in ['+', '-', '*', '/']:
                raise ValueError("Operação inválida. Use apenas +, -, * ou /.")
            
            # Realiza o cálculo
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                # Tratamento da divisão por zero
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            
            # Exibe o resultado e encerra o programa
            print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
            print("Operação concluída com sucesso!")
            break
        
        # Tratamento de erros
        except ValueError as ve:
            print(f"Erro: {ve}. Tente novamente.\n")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}. Tente novamente.\n")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Tente novamente.\n")


# Executa a calculadora
calculadora()
