#Find the shortest path between Bend and San Francisco given the weighted graph

import numpy as np
#Create 5x5 weighted adjacency matrix
weighted_adj_matrix = np.array([
    [0,50,40,0,0],      #Bend
    [50,0,0,0,200],     #Medford
    [40,0,0,130,175],   #Klamath Falls
    [0,0,130,0,180],    #Reno
    [0,200,175,180,0]   #San Francisco
])

#Provide city names for the indices
cities = ["Bend", "Medford", "Klamath Falls", "Reno", "San Francisco"]

#Use Dijkstra's algorithm for finding the shortest path
def dijkstra_algo(matrix, start, end):
    """Runs Dijkstra's algorithm to find the shortest path from the starting vertex (city) to the end vertex."""
    n = len(matrix)                 #Gives the number of cities, one per row
    visited = [False] * n           #Which cities have been visited, none initially
    distance = [float('inf')] * n   #Stores the shortest path from starting vertex to other vertices, initially set to infinite and is updated as algo runs
    prev = [None] * n               #Stores the previous vertices found while searching for shortest path, initially set to none
    distance[start] = 0             #Pathfinding begins at the starting vertex, and the distance to itself is zero

    for _ in range(n):
        #Find the vertex with the smallest distance
        min_distance = float('inf')
        u = -1
        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                u = i

        if u == -1:
            break   #All vertices have been traversed

        visited[u] = True

        #Update distances between vertices
        for v in range(n):
            if matrix[u][v] > 0 and not visited[v]:
                alt = distance[u] + matrix[u][v]
                #Print out the different paths
                print(f"Path: {cities[u]} -> {cities[v]} | Current Distance to {cities[v]}: {distance[v]} | New Distance: {alt}")
                if alt < distance[v]:
                    distance[v] = alt
                    prev[v] = u

    #Build the found path
    path = []
    u = end
    while u is not None:
        path.insert(0, u)
        u = prev[u]
    return distance[end], path

#Set indices based on table given: Bend = 0, Medford = 1, Klamath Falls = 2, Reno = 3, S.F. = 4
shortest_distance, path = dijkstra_algo(weighted_adj_matrix, 0, 4)

paths = [cities[i] for i in path]

print("\nShortest Distance:", shortest_distance)
print("Shortest Path:", " -> ".join(paths))
