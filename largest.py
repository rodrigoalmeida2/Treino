def encontrar_maior(arr):
    # Verificar se o array está vazio
    if len(arr) == 0:
        raise ValueError("O array está vazio.")
    
    # Inicializar o maior número como o primeiro elemento
    maior = arr[0]
    
    # Iterar pelos elementos do array
    for num in arr:
        if num > maior:
            maior = num
    
    return maior

# Exemplo de uso:
array = [3, 1, 7, 0, 5]
print("O maior número é:", encontrar_maior(array))
