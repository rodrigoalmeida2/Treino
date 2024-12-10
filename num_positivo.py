def calcular_media_positivos():
    print("Digite números positivos para calcular a média. Digite 0 para encerrar.")
    soma = 0
    contador = 0

    while True:
        try:
            numero = float(input("Digite um número: "))
            
            if numero == 0:
                break
            elif numero > 0:
                soma += numero
                contador += 1
            else:
                print("Por favor, insira apenas números positivos ou 0 para sair.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")
    
    if contador == 0:
        print("Nenhum número positivo foi digitado.")
    else:
        media = soma / contador
        print(f"A média dos números positivos digitados é: {media:.2f}")

# Chamar a função
calcular_media_positivos()
