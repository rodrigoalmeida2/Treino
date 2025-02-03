class Fila:
    def __init__(self):
        self.itens = []  # Lista para armazenar os elementos da fila

    def enfileirar(self, item):
        """Adiciona um elemento no final da fila."""
        self.itens.append(item)
        print(f"{item} enfileirado.")

    def desenfileirar(self):
        """Remove e retorna o elemento no início da fila."""
        if self.esta_vazia():
            print("A fila está vazia. Não há elementos para desenfileirar.")
            return None
        return self.itens.pop(0)

    def frente(self):
        """Retorna o elemento na frente da fila sem removê-lo."""
        if self.esta_vazia():
            print("A fila está vazia.")
            return None
        return self.itens[0]

    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.itens) == 0

    def tamanho(self):
        """Retorna o número de elementos na fila."""
        return len(self.itens)

# Exemplo de uso
fila = Fila()

# Operações na fila
fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
print(f"Elemento na frente: {fila.frente()}")
print(f"Tamanho da fila: {fila.tamanho()}")

print(f"Desenfileirado: {fila.desenfileirar()}")
print(f"Elemento na frente após desenfileirar: {fila.frente()}")
print(f"A fila está vazia? {'Sim' if fila.esta_vazia() else 'Não'}")
