def bresenham(x0, y0, x1, y1):
    # Lista para armazenar os pontos da linha
    points = []

    # Diferenças entre as coordenadas
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # Definir os incrementos
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    # Erro inicial
    if dx > dy:
        err = dx / 2.0
    else:
        err = -dy / 2.0

    # Laço para percorrer o segmento de reta
    while True:
        # Adiciona o ponto atual à lista
        points.append((x0, y0))

        # Verifica se chegou no ponto final
        if x0 == x1 and y0 == y1:
            break

        # Calcula o erro e decide qual eixo incrementar
        e2 = err
        if e2 > -dx:
            err -= dy
            x0 += sx
        if e2 < dy:
            err += dx
            y0 += sy

    return points


# Exemplo de uso
x0, y0 = 12, 10
x1, y1 = 10, -10
points = bresenham(x0, y0, x1, y1)

# Imprime os pontos da linha
for point in points:
    print(point)
