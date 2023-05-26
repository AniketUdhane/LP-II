class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def kruskal_mst(self):
        # Sort edges in ascending order of weight
        self.edges.sort(key=lambda x: x[2])

        mst = []
        union_find = UnionFind(self.V)

        for edge in self.edges:
            u, v, weight = edge

            if union_find.find(u) != union_find.find(v):
                # Add the edge to the MST
                mst.append(edge)
                union_find.union(u, v)

        return mst

# User input to get the number of vertices and edges
print("Enter the number of vertices:")
num_vertices = int(input())

print("Enter the number of edges:")
num_edges = int(input())

# Create a graph
graph = Graph(num_vertices)

# User input to add edges and their weights
print("Enter the edges and their weights (e.g., '0 1 5' means an edge between vertices 0 and 1 with weight 5):")
for _ in range(num_edges):
    u, v, weight = map(int, input().split())
    graph.add_edge(u, v, weight)

# Find and print the Minimum Spanning Tree (MST)
mst = graph.kruskal_mst()

print("Edges of Minimum Spanning Tree:")
for edge in mst:
    u, v, weight = edge
    print(u, "-", v, "\tWeight:", weight)
