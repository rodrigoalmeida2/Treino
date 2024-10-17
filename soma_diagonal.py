# Soma a diferença das diagonais de uma matriz
def diferenca_diagonais(matriz):
    n = len(matriz)
    soma_diagonal_principal = sum(matriz[i][i] for i in range(n))
    soma_diagonal_secundaria = sum(matriz[i][n-1-i] for i in range(n))
    
    diferenca_absoluta = abs(soma_diagonal_principal - soma_diagonal_secundaria)
    return diferenca_absoluta

# Exemplo de uso:
matriz = [
    [1, 2, 8],
    [4, 5, 6],
    [9, 8, 9]
]

resultado = diferenca_diagonais(matriz)
print("A diferença absoluta entre as somas das diagonais é:", resultado)
