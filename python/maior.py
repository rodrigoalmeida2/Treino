# Entrada dos valores e armazenamento em uma lista
num_valores = int(input("Digite quantos valores vc quer inserir: "))
valores = []
for i in range(num_valores):
    valor = int(input(f"Digite o valor {i + 1}: "))
    valores.append(valor)

# Exibindo os valores informados
print("Valores informados:", valores)

# Encontrando o maior valor
maior = valores[0]
for valor in valores[1:]:
    if valor > maior:
        maior = valor

# Exibindo o maior valor
print(f"{maior} é o maior")
