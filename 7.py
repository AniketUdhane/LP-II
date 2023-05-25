import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight

    def find_min_key(self, key, mst_set):
        min_key = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min_key and not mst_set[v]:
                min_key = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        mst_set = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            u = self.find_min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not mst_set[v]
                    and self.graph[u][v] < key[v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return parent

    def print_mst(self, parent):
        print("Edge \tWeight")
        for v in range(1, self.V):
            print(f"{parent[v]} - {v}\t{self.graph[v][parent[v]]}")

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

parent = g.prim_mst()
g.print_mst(parent)
