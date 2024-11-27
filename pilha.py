class Pilha:
    def __init__(self):
        self.itens = []  # Lista para armazenar os elementos da pilha

    def empilhar(self, item):
        """Adiciona um elemento no topo da pilha."""
        self.itens.append(item)
        print(f"{item} empilhado.")

    def desempilhar(self):
        """Remove e retorna o elemento do topo da pilha."""
        if self.esta_vazia():
            print("A pilha está vazia. Não há elementos para desempilhar.")
            return None
        return self.itens.pop()

    def topo(self):
        """Retorna o elemento no topo da pilha sem removê-lo."""
        if self.esta_vazia():
            print("A pilha está vazia.")
            return None
        return self.itens[-1]

    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.itens) == 0

    def tamanho(self):
        """Retorna o número de elementos na pilha."""
        return len(self.itens)

# Exemplo de uso
pilha = Pilha()

# Operações na pilha
pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)
print(f"Elemento no topo: {pilha.topo()}")
print(f"Tamanho da pilha: {pilha.tamanho()}")

print(f"Desempilhado: {pilha.desempilhar()}")
print(f"Elemento no topo após desempilhar: {pilha.topo()}")
print(f"A pilha está vazia? {'Sim' if pilha.esta_vazia() else 'Não'}")
