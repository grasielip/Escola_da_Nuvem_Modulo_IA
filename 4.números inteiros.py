def verificar_pares_impares():
    print("=== Verificador de Números Pares e Ímpares ===")
    print("Digite números inteiros. Quando quiser encerrar, digite 'fim'.\n")
    
    pares = 0
    impares = 0
    
    while True:
        entrada = input("Digite um número inteiro ou 'fim' para encerrar: ").strip().lower()
        
        if entrada == 'fim':
            break
        
        try:
            numero = int(entrada)
            
            if numero % 2 == 0:
                print(f"{numero} é par.\n")
                pares += 1
            else:
                print(f"{numero} é ímpar.\n")
                impares += 1
                
        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números inteiros ou 'fim' para encerrar.\n")
    
    # Exibe o resultado final em uma linha
    print(f"\n=== Resultado Final ===\nPares: {pares} | Ímpares: {impares} | Total: {pares + impares}\nPrograma encerrado. 👋")


# Executa o programa
verificar_pares_impares()
