import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V  # Initialize distances to infinity
        dist[src] = 0  # Distance from source to itself is 0
        visited = [False] * self.V  # Track visited vertices

        for _ in range(self.V):
            # Find the vertex with the minimum distance value
            min_dist = sys.maxsize
            min_index = -1
            for v in range(self.V):
                if not visited[v] and dist[v] < min_dist:
                    min_dist = dist[v]
                    min_index = v

            # Mark the selected vertex as visited
            visited[min_index] = True

            # Update distance values of the adjacent vertices
            for v in range(self.V):
                if (
                    not visited[v]
                    and self.graph[min_index][v] != 0
                    and dist[min_index] + self.graph[min_index][v] < dist[v]
                ):
                    dist[v] = dist[min_index] + self.graph[min_index][v]

        return dist

    def print_shortest_paths(self, src, dist):
        print("Shortest paths from source vertex", src)
        print("Vertex\tDistance")
        for v in range(self.V):
            print(v, "\t", dist[v])


# Example usage
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

src = 0  # Source vertex
dist = g.dijkstra(src)
g.print_shortest_paths(src, dist)
