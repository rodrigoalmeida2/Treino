# Cardápio com preços dos itens
cardapio = {
    000: 000,
    100: 5.00,  # Cachorro-Quente
    101: 7.50,  # X-Salada
    102: 8.00,  # X-Bacon
    103: 2.50,  # Torrada Simples
    104: 3.00   # Refrigerante
}

while True:
    # Entrada do código do item e quantidade
    print("----------------------------\nDigite 000 para encerrar\n----------------------------")
    codigo = int(input("Digite o código do item: "))
    if codigo == 000:
        break
    quantidade = int(input("Digite a quantidade: "))

    # Verificando se o código existe no cardápio
    if codigo in cardapio:
        # Calculando o valor total
        preco_unitario = cardapio[codigo]
        valor_total = preco_unitario * quantidade
        
        # Exibindo o valor a ser pago
        print(f"Valor a ser pago: R$ {valor_total:.2f}")
    else:
        print("Código do item inválido.")