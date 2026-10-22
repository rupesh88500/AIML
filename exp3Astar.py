import heapq

def a_star_arrows(graph, start, goal, h):
    open_set = [(h(start), start)]
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            full_path = [start] + path[::-1]
            return " - ".join(full_path)
            
        for neighbor, weight in graph[current].items():
            tentative_g = g_score[current] + weight
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                heapq.heappush(open_set, (tentative_g + h(neighbor), neighbor))
                
    return "No path found"

weighted_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 3, 'C': 1},
    'C': {'D': 1},
    'D': {}
}

heuristics = {'A': 4, 'B': 2, 'C': 1, 'D': 0}

path = a_star_arrows(weighted_graph, 'A', 'D', lambda n: heuristics[n])
print("A* Path:", path)
