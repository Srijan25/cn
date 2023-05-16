import heapq

# function to calculate the shortest path
def dijkstra(graph, source):
    # initialize distance vector and predecessor vector
    distance = {}
    predecessor = {}
    for node in graph:
        distance[node] = float('inf')
        predecessor[node] = None
    distance[source] = 0

    # create a priority queue and add the source node
    pq = []
    heapq.heappush(pq, (distance[source], source))

    # iterate over the priority queue until it's empty
    while pq:
        # get the node with the smallest distance
        (dist, u) = heapq.heappop(pq)

        # iterate over the adjacent nodes
        for v in graph[u]:
            # calculate the new distance
            alt = distance[u] + graph[u][v]
            if alt < distance[v]:
                # update the distance vector and predecessor vector
                distance[v] = alt
                predecessor[v] = u
                # add the updated node to the priority queue
                heapq.heappush(pq, (distance[v], v))

    # return the distance vector and predecessor vector
    return distance, predecessor

# function to calculate the shortest path tree
def ospf(graph, source):
    # create a copy of the graph
    graph_copy = graph.copy()

    # calculate the shortest path from source to all other nodes
    distance, predecessor = dijkstra(graph_copy, source)

    # initialize the shortest path tree
    tree = {}
    for node in graph_copy:
        tree[node] = []

    # iterate over the predecessor vector and add the edges to the tree
    for node in predecessor:
        if node != source:
            tree[predecessor[node]].append(node)

    # return the shortest path tree
    return tree

# sample graph
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

# calculate shortest path tree from source node A
tree = ospf(graph, 'A')

# print shortest path tree
print("Shortest path tree:")
for node in tree:
    print(f"{node}: {tree[node]}")
