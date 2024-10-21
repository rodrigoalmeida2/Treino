import math
# Calcúla a distância entre dois pontos no plano
def calcular_distancia(x1, y1, x2, y2):
  distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  return distancia

# Exemplo de uso:
ponto1_x = 5
ponto1_y = 7
ponto2_x = 5
ponto2_y = 7

resultado = calcular_distancia(ponto1_x, ponto1_y, ponto2_x, ponto2_y)
print("A distância entre os pontos é:", resultado)