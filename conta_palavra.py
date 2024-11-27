def contar_palavras(frase):
    # Divide a frase em palavras com base nos espaços
    palavras = frase.split()
    # Conta o número de palavras
    total_palavras = len(palavras)
    return total_palavras

# Exemplo de uso
frase = input("Digite uma frase: ")
quantidade = contar_palavras(frase)
print(f"A frase contém {quantidade} palavras.")
