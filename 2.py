from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

    def bfs(self, start_vertex):
        visited = set()
        queue = deque()

        visited.add(start_vertex)
        queue.append(start_vertex)

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            neighbors = self.graph[current_vertex]
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Create a graph
graph = Graph()

# User input to add edges
print("Enter the number of edges:")
num_edges = int(input())

print("Enter the edges (e.g., '1 2' means an edge between vertices 1 and 2):")
for _ in range(num_edges):
    try:
        u, v = map(int, input().split())
        graph.add_edge(u, v)
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")

# Perform BFS
print("Enter the starting vertex for BFS:")
start_vertex = int(input())

print("BFS traversal:")
graph.bfs(start_vertex)
