# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print("\n")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)
    print("\n")

# Função para verificar o vencedor
def verificar_vencedor(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != " ":
            return linha[0]

    # Verificar colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != " ":
            return tabuleiro[0][col]

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
        return tabuleiro[0][2]

    return None

# Função principal
def jogo_da_velha():
    # Inicializar o tabuleiro
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    # Loop principal do jogo
    while jogadas < 9:
        exibir_tabuleiro(tabuleiro)
        print(f"É a vez do jogador {jogador_atual}")

        # Receber entrada do jogador
        try:
            linha = int(input("Escolha a linha (1-3): ")) - 1
            coluna = int(input("Escolha a coluna (1-3): ")) - 1

            if tabuleiro[linha][coluna] != " ":
                print("Essa posição já está ocupada. Escolha outra.")
                continue
        except (IndexError, ValueError):
            print("Entrada inválida. Por favor, insira valores entre 1 e 3.")
            continue

        # Atualizar o tabuleiro
        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        # Verificar se há um vencedor
        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {vencedor} venceu!")
            return

        # Alternar jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

    # Se o jogo terminar sem vencedor
    exibir_tabuleiro(tabuleiro)
    print("Empate! Nenhum jogador venceu.")

# Iniciar o jogo
jogo_da_velha()
