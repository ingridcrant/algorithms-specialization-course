import heapq

# Median Maintenance Problem
# uses two heaps: one min heap and one max heap
max_heap = []                                   # max heap is implemented as a min heap, but with negative-value nodes
min_heap = []

all_nums = list(map(int, open("Median.txt").read().splitlines()))
sum = all_nums[0]
next_median = min([all_nums[0], all_nums[1]])
next_max = max([all_nums[0], all_nums[1]])

sum += next_median

heapq.heappush(max_heap, (-1)*next_median)
heapq.heappush(min_heap, next_max)

for i in range(2, len(all_nums)):
    next_num = int(all_nums[i])
    line_num = i + 1

    if next_num > min_heap[0]:
        heapq.heappush(min_heap, next_num)
    elif next_num <= (-1)*max_heap[0]:
        heapq.heappush(max_heap, (-1)*next_num)
    else:
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, next_num)
        else:
            heapq.heappush(max_heap, (-1)*next_num)
    
    num_in_max = (line_num + 1) // 2
    num_in_min = line_num - num_in_max

    if len(max_heap) > num_in_max:
        median = (-1) * heapq.heappop(max_heap)
        heapq.heappush(min_heap, median)
    elif len(min_heap) > num_in_min:
        median = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-1)*median)
    
    sum += (-1)*max_heap[0]                         # calculates the median for all numbers 1 to line_num and adds it to the sum

print(sum%10000)