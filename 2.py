from collections import deque

def bfs_recursive(graph, queue, visited):
    if not queue:
        return
    
    node = queue.popleft()
    visited.add(node)
    print(node)  # Process the node (you can modify this part as needed)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    
    bfs_recursive(graph, queue, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    bfs_recursive(graph, queue, visited)

# Example graph representation using dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': ['E']
}

# Call BFS with the graph and starting node
bfs(graph, 'A')
