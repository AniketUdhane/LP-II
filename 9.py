import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    visited = set()

    while queue:
        (cost, node) = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                new_cost = distances[node] + weight
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, neighbor))

    return distances

# Example usage
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter name of node {i+1}: ")
    edges = {}
    while True:
        neighbor = input(f"Enter neighbor of {node} (or type 'done' to finish): ")
        if neighbor == 'done':
            break
        weight = int(input(f"Enter weight of edge between {node} and {neighbor}: "))
        edges[neighbor] = weight
    graph[node] = edges

start = input("Enter starting node: ")
distances = dijkstra(graph, start)

print(distances)
