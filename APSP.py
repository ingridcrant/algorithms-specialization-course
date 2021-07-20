from math import inf
from copy import deepcopy
import heapq
from collections import defaultdict

def Dijkstra(graph, start):
    n = len(graph)
    visited = set()
    shortest_distances = {}

    for vertex in graph:
        shortest_distances[vertex] = inf
    
    shortest_distances[start] = 0
    min_dist = [(0,(start, start))]      # [(dist, node)]
    previous = {}

    while len(visited) < n:
        current_dist, current_edge = heapq.heappop(min_dist)
        previous[current_edge[1]] = current_edge[0]
        current_node = current_edge[1]

        if current_node not in visited:
            visited.add(current_node)

            for pair in graph[current_node].items():
                connection = pair[0]
                if connection not in visited:
                    dist = current_dist + pair[1]

                    if dist < shortest_distances[connection]:
                        shortest_distances[connection] = dist
                        heapq.heappush(min_dist, (dist, (current_node, connection)))
    
    del shortest_distances[start]
    return sorted(list(shortest_distances.items()), key = lambda l:l[1])[0], previous

def BF(num_vertices, graph, start):
    A = []
    for i in range(2):
        A.append({})
    
    for vertex in graph:
        A[1][vertex] = inf
    A[1][start] = 0
    
    for i in range(1, num_vertices+1):
        A[0] = A[1]
        A[1] = {}

        for vertex in graph:
            case1 = A[0][vertex]
            case2 = inf

            for tail in graph:
                if vertex in graph[tail]:
                    new_cost = A[0][tail] + graph[tail][vertex]
                    case2 = min(case2, new_cost)
            
            A[1][vertex] = min(case1, case2)
    
    for vertex in graph:
        if A[0][vertex] != A[1][vertex]:
            return "negative cycle"
    
    return A[1]

def Johnson(filename):
    graph = {}
    num_vertices = 0
    num_edges = 0

    first_line = True

    with open(filename) as a_file:
        for line in a_file:
            if first_line:
                [num_vertices, num_edges] = [int(x) for x in line.strip().split()]
            else:
                [tail, head, length] = [int(x) for x in line.strip().split()]
                
                if tail not in graph:
                    graph[tail] = {head: length}
                else:
                    temp_edges = graph[tail]
                    temp_edges[head] = length
                    graph[tail] = temp_edges
            
            first_line = False
    
    BFGraph = deepcopy(graph)
    s_edges = {}

    for i in range(1, num_vertices+1):
        s_edges[i] = 0
    BFGraph["s"] = s_edges

    Pv = BF(num_vertices, BFGraph, "s")

    if Pv == "negative cycle":
        return Pv

    for tail in graph:
        for head in graph[tail]:
            ce = graph[tail][head]
            cef = ce + Pv[tail] - Pv[head]
            graph[tail][head] = cef
    
    shortest_distance = inf
    for vertex in graph:
        shortest_distance_next, path = Dijkstra(graph, vertex)
        pathlength = 0
        head = shortest_distance_next[0]
        tail = path[head]

        while head != vertex:
            pathlength += graph[tail][head] - Pv[tail] + Pv[head]
            head = tail
            tail = path[head]

        shortest_distance = min(shortest_distance, pathlength)
    
    return shortest_distance

# correctly detects negative cycles, but doesn't compute correct shortest path
print(Johnson("g3.txt"))
# outputs -7, when the correct answer is -17. Will revisit.