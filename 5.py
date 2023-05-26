#single source shortest
import sys

# Function to find the vertex with the minimum distance value
def minDistance(dist, visited):
    min_dist = sys.maxsize
    min_index = -1
    for v in range(len(dist)):
        if dist[v] < min_dist and not visited[v]:
            min_dist = dist[v]
            min_index = v
    return min_index

# Function to print the shortest distance from the source to all vertices
def printDistances(dist):
    print("Vertex \t Distance from Source")
    for i in range(len(dist)):
        print(i, "\t\t", dist[i])

# Function to implement the greedy search algorithm
def greedySearch(graph, source):
    num_vertices = len(graph)
    dist = [sys.maxsize] * num_vertices
    visited = [False] * num_vertices
    dist[source] = 0
    
    for i in range(num_vertices):
        # Find the vertex with the minimum distance value
        u = minDistance(dist, visited)
        visited[u] = True
        
        # Update the distance values of the adjacent vertices
        for v in range(num_vertices):
            if graph[u][v] > 0 and not visited[v] and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
    
    printDistances(dist)

# Main program
if __name__ == '__main__':
    # Get the number of vertices and edges
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    # Create the adjacency matrix
    graph = [[0] * num_vertices for _ in range(num_vertices)]
    
    # Get the graph data
    for i in range(num_edges):
        print("Enter the edge data in the format <from> <to> <weight>: ")
        u, v, w = map(int, input().split())
        graph[u][v] = w
    
    # Get the source vertex
    source = int(input("Enter the source vertex: "))
    
    # Find the shortest distances from the source vertex to all other vertices
    greedySearch(graph, source)
