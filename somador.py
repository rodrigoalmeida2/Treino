# Definindo a função SuperSomador
def SuperSomador(num1, num2):
    # Garantir que o menor valor seja o ponto inicial
    menor = min(num1, num2)
    maior = max(num1, num2)
    
    # Calcula a soma dos valores no intervalo
    soma = sum(range(menor, maior + 1))
    return soma

# Testando a função
# Exemplo 1
resultado1 = SuperSomador(5, 20)
print(f"SuperSomador(1, 6) = {resultado1}")  # Deve retornar 21

# Exemplo 2
resultado2 = SuperSomador(15, 19)
print(f"SuperSomador(15, 19) = {resultado2}")  # Deve retornar 85
