def triangle_of_stars(N):
    # Loop de 1 até n para printar as linhas
    for i in range(1, N + 1):
        print('*' * i)

# pega valor de n
N = int(input("Enter an integer N: "))

triangle_of_stars(N)
