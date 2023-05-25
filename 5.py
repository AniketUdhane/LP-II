import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight

    def find_min_distance(self, dist, visited):
        min_distance = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if dist[v] < min_distance and not visited[v]:
                min_distance = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = self.find_min_distance(dist, visited)
            visited[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not visited[v]
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

# Example usage
g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 2)
g.add_edge(2, 4, 1)
g.add_edge(3, 4, 3)
g.add_edge(3, 5, 4)
g.add_edge(4, 5, 1)

src = 0
distances = g.dijkstra(src)

for v in range(g.V):
    print(f"Distance from source vertex {src} to vertex {v}: {distances[v]}")
