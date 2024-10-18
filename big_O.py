def find_largest(arr, inicio, fim):
    # Caso base: Se houver apenas um elemento no array
    if inicio == fim:
        return arr[inicio]

    # Encontra o ponto médio do array
    meio = (inicio + fim) // 2

    # Recursivamente encontra o maior número nas duas metades
    maior_esquerda = find_largest(arr, inicio, meio)
    maior_direita = find_largest(arr, meio + 1, fim)

    # Retorna o maior entre os dois
    return max(maior_esquerda, maior_direita)

# Exemplo de uso:
arr = [3, 5, 9, 1, 8, 12, 4]
resultado = find_largest(arr, 0, len(arr) - 1)
print("O maior número no array é:", resultado)
