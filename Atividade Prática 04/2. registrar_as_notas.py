def registrar_notas():
    notas = []  # Lista para armazenar as notas
    
    print("=== Sistema de Registro de Notas ===")
    print("Digite as notas dos alunos (0 a 10).")
    print("Quando terminar, digite 'fim'.\n")
    
    while True:
        entrada = input("Digite uma nota ou 'fim' para encerrar: ").strip().lower()
        
        if entrada == 'fim':
            break
        
        try:
            nota = float(entrada)
            
            # Verifica se a nota está dentro do intervalo permitido
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("⚠️ Nota inválida! Digite um valor entre 0 e 10.")
        
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número válido ou 'fim' para encerrar.")
    
    if notas:
        media = sum(notas) / len(notas)
        print(f"\n📊 Média da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")


# Executa o programa
registrar_notas()

