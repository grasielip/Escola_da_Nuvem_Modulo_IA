print(" Defina sua senha \n------------------------------")

def verificar_senha():
    print("=== Verificador de Senha Forte ===")
    print("A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")
    print("Digite 'sair' para encerrar.\n")
    
    while True:
        senha = input("Digite uma senha: ").strip()
        
        # Permite encerrar o programa
        if senha.lower() == 'sair':
            print("Encerrando o programa. Até mais!")
            break
        
        # Verifica comprimento mínimo
        if len(senha) < 8:
            print("⚠️ Senha muito curta! Deve ter pelo menos 8 caracteres.\n")
            continue
        
        # Verifica se contém pelo menos um número
        if not any(char.isdigit() for char in senha):
            print("⚠️ A senha deve conter pelo menos um número.\n")
            continue
        
        # Se passou por todas as verificações, é forte
        print("✅ Senha forte! Boa escolha de segurança.")
        break


# Executa o programa
verificar_senha()
