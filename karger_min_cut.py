from random import choice
from copy import deepcopy

def remove_item(arr, item):
    arr_copy = arr[:]

    for el in arr:
        if el == item:
            arr_copy.remove(el)
    
    return arr_copy

def replace_items(arr, items, replacement):
    arr_copy = arr[:]

    for el in arr:
        if el in items:
            arr_copy.remove(el)
            arr_copy.append(replacement)
    
    return arr_copy

def contract(graph):
    v1 = choice(list(graph.keys()))
    v2 = choice(graph[v1])
    combined_vertex = v1 + "+" + v2

    graph[v1] = remove_item(graph[v1], v2)
    graph[v2] = remove_item(graph[v2], v1)
    graph[combined_vertex] = graph[v1] + graph[v2]

    del graph[v1]
    del graph[v2]

    for vertex in graph.keys():
        if vertex != combined_vertex:
            graph[vertex] = replace_items(graph[vertex], set([v1, v2]), combined_vertex)

def find_min_cut(graph):
    n = len(graph)              # number of vertices
    min_crosses = (n*(n-1))//2      # largest possible num of crossing edges in a cut
    
    for i in range(n):
        copied_graph = deepcopy(graph)
        while len(copied_graph) > 2:
            contract(copied_graph)
        min_crosses = min(min_crosses, len(list(copied_graph.values())[0]))
    
    return min_crosses

graph = {}

with open("KargerMinCut.txt") as a_file:
    for line in a_file:
        adj_vertices = line.strip().split('\t')
        graph[adj_vertices[0]] = adj_vertices[1:]

a_file.close()

print(find_min_cut(graph))