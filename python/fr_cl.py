# Solicita ao usuário a temperatura em Fahrenheit
temp_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Converte a temperatura para Celsius
temp_celsius = (temp_fahrenheit - 32) * 5 / 9

# Exibe o resultado
print(f"A temperatura em graus Celsius é: {temp_celsius:.2f}")
