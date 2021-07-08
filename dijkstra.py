from math import inf
import heapq

def MainLoop(graph):
    n = len(graph)
    visited = set()
    shortest_distances = [0]+[inf]*(n-1)
    min_dist = [(0,1)]      # [(dist, node)]

    while len(visited) < n:
        current_dist, current_node = heapq.heappop(min_dist)

        if current_node not in visited:
            visited.add(current_node)

            for pair in graph[current_node]:
                connection = pair[0]
                if connection not in visited:
                    dist = current_dist + pair[1]
                    if dist < shortest_distances[connection-1]:
                        shortest_distances[connection-1] = dist
                        heapq.heappush(min_dist, (dist, connection))
    
    return shortest_distances

graph = {}

# graph in the form {t1: [[h1, l1], [h2, l2]], t2: [[h1, l1], [h2, l2]]}
with open("DK.txt") as a_file:
    for line in a_file:
        lis = line.strip().split('\t')
        
        v1 = int(lis[0])
        v2s = []

        for i in range(1, len(lis)):
            [v2, length] = lis[i].split(",")
            v2s.append([int(v2), int(length)])
        
        graph[v1] = v2s

shortest_distances = MainLoop(graph)

vertices = [7,37,59,82,99,115,133,165,188,197]

for vertex in vertices:
    print(shortest_distances[vertex-1], end=",")