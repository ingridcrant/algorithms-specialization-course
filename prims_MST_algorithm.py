from math import inf
import heapq

def Prims(adjacency_list):
    x = [1]
    sum = 0
    key = {}

    for vertex in adjacency_list:
        key[vertex] = inf

    heap = []

    for edge in adjacency_list[1]:
        second_node = edge[0]
        length = edge[1]
        if second_node not in x:
            heapq.heappush(heap, (length, second_node))
            temp_val = key[second_node]
            new_key = min(temp_val, length)

            key[second_node] = new_key

    while len(x) < len(adjacency_list):
        (min_length, new_node_x) = heapq.heappop(heap)
        x.append(new_node_x)
        sum += min_length

        for edge in adjacency_list[new_node_x]:
            second_node = edge[0]
            length = edge[1]
            if second_node not in x:
                if (key[second_node], second_node) in heap:
                    i = heap.index((key[second_node], second_node))
                    heap[i] = heap[-1]
                    heap.pop()
                    heapq.heapify(heap)
                
                prev_key = key[second_node]
                new_key = min(prev_key, length)
                key[second_node] = new_key

                heapq.heappush(heap, (new_key, second_node))

    return sum

adjacency_list = {}

with open("edges.txt") as a_file:
    line_num = 0
    for line in a_file:
        line_num += 1
        if line_num > 1:
            [first_node, second_node, edge_cost] = [int(x) for x in line.strip().split()]
            if first_node not in adjacency_list:
                adjacency_list[first_node] = [[second_node, edge_cost]]
            else:
                temp = adjacency_list[first_node]
                temp.append([second_node, edge_cost])
                adjacency_list[first_node] = temp
            
            if second_node not in adjacency_list:
                adjacency_list[second_node] = [[first_node, edge_cost]]
            else:
                temp = adjacency_list[second_node]
                temp.append([first_node, edge_cost])
                adjacency_list[second_node] = temp

print(Prims(adjacency_list))
