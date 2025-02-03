import java.util.EmptyStackException;

public class Stack<T> {
    private Node<T> top; // Topo da pilha
    private int size;    // Tamanho da pilha

    // Classe interna para representar um nó da pilha
    private static class Node<T> {
        private T data;
        private Node<T> next;

        public Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    // Construtor
    public Stack() {
        this.top = null;
        this.size = 0;
    }

    // Método para adicionar um elemento na pilha (push)
    public void push(T data) {
        Node<T> newNode = new Node<>(data);
        newNode.next = top;
        top = newNode;
        size++;
    }

    // Método para remover o elemento do topo da pilha (pop)
    public T pop() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        T data = top.data;
        top = top.next;
        size--;
        return data;
    }

    // Método para consultar o elemento no topo da pilha sem removê-lo (peek)
    public T peek() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return top.data;
    }

    // Método para verificar se a pilha está vazia
    public boolean isEmpty() {
        return top == null;
    }

    // Método para obter o tamanho da pilha
    public int size() {
        return size;
    }

    // Exemplo de uso da pilha
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

        // Adicionando elementos na pilha
        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println("Elemento no topo: " + stack.peek()); // Deve imprimir 30

        System.out.println("Removendo elemento: " + stack.pop()); // Deve imprimir 30
        System.out.println("Elemento no topo após remoção: " + stack.peek()); // Deve imprimir 20

        System.out.println("Tamanho da pilha: " + stack.size()); // Deve imprimir 2

        // Verificando se a pilha está vazia
        System.out.println("A pilha está vazia? " + stack.isEmpty()); // Deve imprimir false

        // Esvaziando a pilha
        stack.pop();
        stack.pop();
        System.out.println("A pilha está vazia agora? " + stack.isEmpty()); // Deve imprimir true
    }
}

