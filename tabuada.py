# Entrada do número para calcular a tabuada
numero = int(input("Digite um número para ver sua tabuada: "))

# Exibindo a tabuada
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
