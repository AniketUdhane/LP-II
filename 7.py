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

