from math import inf

x = set()
shortest_distances = [0] + [inf]*199

def MainLoop(graph):
    global x, shortest_distances
    x.add(1)
    n = len(graph)

    while len(x) < n:
        shortest_distance_so_far = inf
        new_node = None

        for tail in x:
            for pair in graph[tail]:
                v2 = pair[0]
                length = shortest_distances[tail-1] + pair[1]

                if v2 not in x:
                    if length < shortest_distance_so_far:
                        shortest_distance_so_far = length
                        new_node = v2
        
        x.add(new_node)     
        shortest_distances[new_node-1] = shortest_distance_so_far

graph = {}

# graph in the form {t1, [[h1, l1], [h2, l2]], t2, [[h1, l1], [h2, l2]]}
with open("DK.txt") as a_file:
    for line in a_file:
        lis = line.strip().split('\t')
        
        v1 = int(lis[0])
        v2s = []

        for i in range(1, len(lis)):
            [v2, length] = lis[i].split(",")
            v2s.append([int(v2), int(length)])
        
        graph[v1] = v2s

MainLoop(graph)