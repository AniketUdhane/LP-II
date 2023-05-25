class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append((src, dest, weight))

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        result = []  # Store the MST
        parent = []  # Track the parent of each vertex
        rank = []  # Track the rank of each vertex

        self.graph = sorted(self.graph, key=lambda item: item[2])  # Sort edges by weight

        for v in range(self.V):
            parent.append(v)
            rank.append(0)

        i = 0  # Index variable to iterate through sorted edges
        e = 0  # Variable to track the number of edges included in the MST

        while e < self.V - 1:
            src, dest, weight = self.graph[i]
            i += 1

            x = self.find_parent(parent, src)
            y = self.find_parent(parent, dest)

            if x != y:
                e += 1
                result.append((src, dest, weight))
                self.union(parent, rank, x, y)

        return result

    def print_mst(self, mst):
        print("Edge \tWeight")
        for src, dest, weight in mst:
            print(f"{src} - {dest}\t{weight}")


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

mst = g.kruskal_mst()
g.print_mst(mst)
