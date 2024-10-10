# Esse código define uma função chamada smaller que, dado um array err
# retorna uma lista menor_c com a quantidade de números menores que cada elemento da lista err.
def smaller(err):
    qantos_num_menores = []
    for menor in err:
        atual = menor
        menor_count = 0
        for menor in err:
            if atual > menor:        
                menor_count += 1
        qantos_num_menores.append(menor_count)
    return qantos_num_menores

# Retorna a quantidade de numeros menores a diretita de err[i]
def count_smaller_numbers(arr):
    qantos_num_menores = []
    n = len(arr)
    
    for i in range(n):
        count = 0
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                count += 1
        qantos_num_menores.append(count)
    
    return qantos_num_menores

if __name__=="__main__":
    #Exemplo 1
    menor = [1, 2, 0]
    print(smaller(menor))
    #exemplo 2
    arr = [1, 2, 0]
    print(count_smaller_numbers(arr))