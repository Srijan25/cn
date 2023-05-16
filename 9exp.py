import sys

# function to calculate the shortest distance
def bellman_ford(graph, source):
    # initialize distance vector and predecessor vector
    distance = {}
    predecessor = {}
    for node in graph:
        distance[node] = sys.maxsize
        predecessor[node] = None
    distance[source] = 0

    # iterate over all edges V-1 times
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                # relax the edge from u to v
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]
                    predecessor[v] = u

    # check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            if distance[u] + graph[u][v] < distance[v]:
                print("Graph contains negative-weight cycle")
                return

    # return the distance vector and predecessor vector
    return distance, predecessor

# sample graph
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 7},
    'C': {'D': 3},
    'D': {}
}

# calculate shortest distance from source node A
distance, predecessor = bellman_ford(graph, 'A')

# print distance vector and predecessor vector
print("Distance vector:")
for node in distance:
    print(f"{node}: {distance[node]}")
print("\nPredecessor vector:")
for node in predecessor:
    print(f"{node}: {predecessor[node]}")
