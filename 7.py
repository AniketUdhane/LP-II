'''
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

'''

import heapq

def prim(graph, start):
    visited = {start}
    edges = [(cost, start, neighbor) for neighbor, cost in graph[start].items()]
    heapq.heapify(edges)
    mst_cost = 0
    mst_edges = []

    while edges:
        cost, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        mst_cost += cost
        mst_edges.append((u, v, cost))

        for neighbor, cost in graph[v].items():
            if neighbor not in visited:
                heapq.heappush(edges, (cost, v, neighbor))

    return mst_cost, mst_edges

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
mst_cost, mst_edges = prim(graph, start)

print(f"MST cost: {mst_cost}")
print("MST edges:")
for u, v, cost in mst_edges:
    print(f"{u} --{cost}-- {v}")

