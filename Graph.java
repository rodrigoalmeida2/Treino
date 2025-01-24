import java.util.*;

public class Graph {
    private Map<String, List<String>> adjList;

    // Construtor
    public Graph() {
        this.adjList = new HashMap<>();
    }

    // Adicionar um vértice
    public void addVertex(String vertex) {
        adjList.putIfAbsent(vertex, new ArrayList<>());
    }

    // Adicionar uma aresta
    public void addEdge(String vertex1, String vertex2) {
        adjList.putIfAbsent(vertex1, new ArrayList<>());
        adjList.putIfAbsent(vertex2, new ArrayList<>());
        adjList.get(vertex1).add(vertex2);
        adjList.get(vertex2).add(vertex1); // Para grafo não direcionado, comentar esta linha para grafo direcionado
    }

    // Exibir o grafo
    public void displayGraph() {
        for (String vertex : adjList.keySet()) {
            System.out.println(vertex + " -> " + adjList.get(vertex));
        }
    }

    public static void main(String[] args) {
        Graph graph = new Graph();

        // Adicionando vértices
        graph.addVertex("A");
        graph.addVertex("B");
        graph.addVertex("C");
        graph.addVertex("D");

        // Adicionando arestas
        graph.addEdge("A", "B");
        graph.addEdge("A", "C");
        graph.addEdge("B", "C");
        graph.addEdge("C", "D");

        // Exibindo o grafo
        graph.displayGraph();
    }
}
