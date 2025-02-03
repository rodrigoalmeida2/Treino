# Pega um array e organiza do maior para o menor
def heapify(arr, n, i):
    maior = i  # Inicializa o maior como raiz
    esquerda = 2 * i + 1  # Filho esquerdo
    direita = 2 * i + 2  # Filho direito

    # Se o filho esquerdo for maior que a raiz
    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    # Se o filho direito for maior que o maior atual
    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    # Se o maior não for a raiz
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]  # Troca
        # Recursivamente faz heapify na subárvore afetada
        heapify(arr, n, maior)

def construir_max_heap(arr):
    n = len(arr)

    # Construir o heap (rearranjando o array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    return arr

# Função para exibir a árvore em forma de Max Heap
def exibir_arvore(arr, n, i, nivel=0):
    if i < n:
        # Exibe o filho da direita (recursivamente)
        exibir_arvore(arr, n, 2 * i + 2, nivel + 1)

        # Exibe o nó atual com indentação de acordo com o nível
        print(' ' * 4 * nivel + '->', arr[i])

        # Exibe o filho da esquerda (recursivamente)
        exibir_arvore(arr, n, 2 * i + 1, nivel + 1)

# Exemplo de uso:
numeros = [3, 9, 2, 1, 4, 5]
construir_max_heap(numeros)

print("Max Heap visualizada como uma árvore:")
exibir_arvore(numeros, len(numeros), 0)
