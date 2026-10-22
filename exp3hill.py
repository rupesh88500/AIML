def hill_climbing_arrows(graph, start, value_func):
    current = start
    path = [current]
    
    while True:
        neighbors = graph.get(current, [])
        if not neighbors:
            break
            
        best_neighbor = max(neighbors, key=value_func)
        
        if value_func(best_neighbor) <= value_func(current):
            break
            
        current = best_neighbor
        path.append(current)
        
    return " - ".join(path)

my_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

node_values = {'A': 1, 'B': 3, 'C': 2, 'D': 4, 'E': 7, 'F': 5}

arrow_path = hill_climbing_arrows(my_graph, 'A', lambda node: node_values[node])
print("Hill Climbing Path:", arrow_path)
