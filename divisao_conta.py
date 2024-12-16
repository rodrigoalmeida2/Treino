def dividir_conta():
    # Receber o valor total da conta
    valor_conta = float(input("Digite o valor total da conta: R$ "))
    
    # Receber o número de pessoas
    num_pessoas = int(input("Quantas pessoas irão pagar a conta? "))
    
    # Validar o número de pessoas
    if num_pessoas <= 0:
        print("Número de pessoas inválido. A conta deve ser dividida por pelo menos uma pessoa.")
        return
    
    # Escolher o método de divisão
    print("\nEscolha a forma de divisão da conta:")
    print("1. Divisão igualitária")
    print("2. Divisão percentual personalizada")
    print("3. Divisão individual personalizada")
    opcao = int(input("Digite o número da opção desejada: "))
    
    # Divisão igualitária
    if opcao == 1:
        valor_por_pessoa = valor_conta / num_pessoas
        print(f"\nDivisão igualitária: cada pessoa deve pagar R$ {valor_por_pessoa:.2f}.")
    
    # Divisão percentual personalizada
    elif opcao == 2:
        print("\nVocê escolheu a divisão percentual personalizada.")
        porcentagens = []
        for i in range(num_pessoas):
            porcentagem = float(input(f"Digite a porcentagem de contribuição da pessoa {i + 1}: "))
            porcentagens.append(porcentagem)
        
        if sum(porcentagens) != 100:
            print("Erro: as porcentagens devem somar 100%.")
            return
        
        print("\nValores a serem pagos:")
        for i, porcentagem in enumerate(porcentagens):
            valor_pagar = (porcentagem / 100) * valor_conta
            print(f"Pessoa {i + 1}: R$ {valor_pagar:.2f}")
    
    # Divisão individual personalizada
    elif opcao == 3:
        print("\nVocê escolheu a divisão individual personalizada.")
        valores = []
        for i in range(num_pessoas):
            valor = float(input(f"Digite o valor que a pessoa {i + 1} vai pagar: R$ "))
            valores.append(valor)
        
        if sum(valores) != valor_conta:
            print("Erro: a soma dos valores individuais deve ser igual ao total da conta.")
            return
        
        print("\nValores a serem pagos:")
        for i, valor in enumerate(valores):
            print(f"Pessoa {i + 1}: R$ {valor:.2f}")
    
    else:
        print("Opção inválida. Escolha entre 1, 2 ou 3.")

# Executar o programa
if __name__ == "__main__":
    dividir_conta()
