# Entrada dos coeficientes
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))
e = float(input("Digite o valor de e: "))
f = float(input("Digite o valor de f: "))

# Calculando o determinante principal
determinante = a * e - b * d

# Verifica se o sistema tem uma solução única
if determinante != 0:
    # Calcula os valores de x e y usando a regra de Cramer
    x = (c * e - b * f) / determinante
    y = (a * f - c * d) / determinante
    
    # Exibe os valores de x e y
    print(f"x = {x}")
    print(f"y = {y}")
else:
    print("O sistema não tem uma solução única.")
