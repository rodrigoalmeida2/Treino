# Solicita ao usuário o valor em centímetros
valor_cm = float(input("Digite o valor em centímetros: "))

# Converte o valor para pés
valor_foot = valor_cm / 30.48

# Exibe o resultado
print(f"O valor em pés é: {valor_foot:.2f}")
