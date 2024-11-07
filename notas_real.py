# Entrada do valor em reais
valor = int(input("Digite o valor em reais: "))
valor_original = valor  # Armazena o valor original para exibição depois

# Inicializa a contagem das notas como uma lista
notas = [0] * 5  # Lista com 5 posições para armazenar as notas de 100, 50, 10, 5 e 1
valores_notas = [100, 50, 10, 5, 1]  # Valores das notas

# Calcula a quantidade mínima de cada nota necessária
for i in range(len(valores_notas)):
    notas[i] = valor // valores_notas[i]
    valor %= valores_notas[i]

# Exibindo o valor lido e a quantidade mínima de notas
print(f"Valor lido: R$ {valor_original}")
print("Menor número de notas necessárias:")

# Imprime somente as notas que são utilizadas (quantidade maior que zero)
for i in range(len(notas)):
    if notas[i] != 0:
        print(f"Notas de R$ {valores_notas[i]}: {notas[i]}")

