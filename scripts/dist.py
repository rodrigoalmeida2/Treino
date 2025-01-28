import math
# Calcúla a distância entre dois pontos no plano
def calcular_distancia(x1, y1, x2, y2):
  distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  return distancia

# Exemplo de uso:
x1 = 5
y1 = 7
x2 = 5
y2 = 7

resultado = calcular_distancia(x1, y1, x2, y2)
print("A distância entre os pontos é:", resultado)