# Solicita ao usuário a escolha da conversão
print("Escolha a opção de conversão:")
print("1 - Centímetros para Pés")
print("2 - Pés para Centímetros")
opcao = int(input("Digite a opção desejada (1 ou 2): "))

if opcao == 1:
    # Conversão de Centímetros para Pés
    valor_cm = float(input("Digite o valor em centímetros: "))
    valor_foot = valor_cm / 30.48
    print(f"O valor em pés é: {valor_foot:.2f}")
elif opcao == 2:
    # Conversão de Pés para Centímetros
    valor_foot = float(input("Digite o valor em pés: "))
    valor_cm = valor_foot * 30.48
    print(f"O valor em centímetros é: {valor_cm:.2f}")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")

