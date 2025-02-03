def selection_sort(arr):
    # Percorre todo o array
    for i in range(len(arr)):
        # Assume que o menor valor está na posição atual
        min_index = i
        # Verifica os elementos restantes
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Troca os elementos
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemplo de uso
valores = [64, 34, 25, 12, 22, 11, 90]
selection_sort(valores)
print("Array ordenado:", valores)
