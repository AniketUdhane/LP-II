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

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()

        visited.add(start_vertex)
        print(start_vertex, end=" ")

        neighbors = self.graph[start_vertex]
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Create a graph
graph = Graph()

# User input to add edges
print("Enter the number of edges:")
num_edges = int(input())

print("Enter the edges (e.g., '1 2' means an edge between vertices 1 and 2):")
for _ in range(num_edges):
    u, v = map(int, input().split())
    graph.add_edge(u, v)

# Perform DFS
print("Enter the starting vertex for DFS:")
start_vertex = int(input())

print("DFS traversal:")
graph.dfs(start_vertex)
