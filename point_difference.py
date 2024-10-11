import math

# Função para calcular a distância euclidiana entre dois pontos
def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Função que resolve o problema de forma recursiva com divisão e conquista
def closest_pair(points):
    def closest_pair_rec(Px, Py):
        # Se tivermos 3 ou menos pontos, resolvemos diretamente (força bruta)
        if len(Px) <= 3:
            min_dist = float('inf')
            closest_points = None
            for i in range(len(Px)):
                for j in range(i + 1, len(Px)):
                    d = distancia(Px[i], Px[j])
                    if d < min_dist:
                        min_dist = d
                        closest_points = (Px[i], Px[j])
            return min_dist, closest_points

        # Dividindo os pontos ao meio
        mid = len(Px) // 2
        Lx = Px[:mid]
        Rx = Px[mid:]
        midpoint = Px[mid][0]

        # Pontos à esquerda e à direita, respectivamente
        Ly = list(filter(lambda x: x[0] <= midpoint, Py))
        Ry = list(filter(lambda x: x[0] > midpoint, Py))

        # Encontrando o par mais próximo na parte esquerda e direita
        (dL, pairL) = closest_pair_rec(Lx, Ly)
        (dR, pairR) = closest_pair_rec(Rx, Ry)

        # Determinando a menor distância entre as duas metades
        d_min = min(dL, dR)
        best_pair = pairL if dL < dR else pairR

        # Verificando a "faixa" ao redor da linha divisória
        strip = [p for p in Py if abs(p[0] - midpoint) < d_min]
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):  # Considera até 7 pontos próximos na faixa
                d = distancia(strip[i], strip[j])
                if d < d_min:
                    d_min = d
                    best_pair = (strip[i], strip[j])

        return d_min, best_pair

    # Ordenando os pontos pelas coordenadas x e y
    Px = sorted(points, key=lambda x: x[0])
    Py = sorted(points, key=lambda x: x[1])

    return closest_pair_rec(Px, Py)

# Função para imprimir o plano com os pontos
def imprimir_plano(pontos, n=9):
    # Cria uma matriz de tamanho n x n cheia de espaços
    plano = [[" " for _ in range(n)] for _ in range(n)]

    # Marca os pontos no plano
    for i, (x, y) in enumerate(pontos):
        label = chr(ord('A') + i)  # Atribui uma letra a cada ponto
        plano[n - y][x - 1] = label

    # Imprime o plano, mostrando os eixos x e y
    print("Plano de Pontos (Y vs X):")
    for i in range(n):
        # Imprimindo as linhas do eixo Y com os pontos
        print(f"{n - i} ", end=" ")
        print(" ".join(plano[i]))
    
    # Imprimindo os valores do eixo X
    print("   " + " ".join(str(i+1) for i in range(n)))

# Exemplo de pontos dados no plano
pontos = [(1, 2), (8, 8), (3, 5), (4, 9), (9, 9), (5, 4), (6, 7)]

# Chamando a função para imprimir o plano
imprimir_plano(pontos)

# Chamando a função para encontrar os dois pontos mais próximos
distancia_minima, pontos_mais_proximos = closest_pair(pontos)
print(f"\nDistância mínima: {distancia_minima}")
print(f"Pontos mais próximos: {pontos_mais_proximos}")
