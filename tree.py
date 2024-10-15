def solve_graph(start, end, arcs):
    # If start and end are the same, we can immediately return True
    if start == end:
        return True
    
    # Create adjacency list
    graph = {}
    for u, v in arcs:
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
    
    # If the start node or end node isn't in the graph, return False
    if start not in graph:
        return False
    
    # DFS to find if there's a path from start to end
    visited = set()
    
    def dfs(node):
        if node == end:
            return True
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False
    
    # Start the DFS
    return dfs(start)

# Example usage
arcs = [(1, 2), (2, 3), (3, 4)]
print(solve_graph(1, 4, arcs))  # Output: True
print(solve_graph(1, 5, arcs))  # Output: False
