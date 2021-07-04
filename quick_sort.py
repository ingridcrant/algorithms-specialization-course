from random import randint

# gets num comparisons in quick sort
def num_of_comparisons(arr):
    return quick_sort(arr, 0, len(arr)-1, 0)[1]

# gets sorted list using quick sort
def quick_sort_arr(arr):
    return quick_sort(arr, 0, len(arr)-1, 0)[0]

# swaps the positions of two elements in the array
def swap(arr, first, last):
    temp = arr[first]
    arr[first] = arr[last]
    arr[last] = temp

# picks the first element in the subarray as the pivot
def pick_first(arr, l):
    return [arr[l], arr]

# picks the last element in the subarray as the pivot
def pick_last(arr, l, r):
    swap(arr, l, r)
    return [arr[l], arr]

# picks the median out of the first, middle, and last element in the subarray to be the pivot
def pick_median(arr, l, r):
    first = arr[l]
    middle = arr[((l+r+2)//2-1)]
    last = arr[r]

    if first < middle < last or last < middle < first:
        swap(arr, l, ((l+r+2)//2-1))
    elif first < last < middle or middle < last < first:
        swap(arr, l, r)
    
    return [arr[l], arr]

# picks a random pivot
def pick_random(arr, l, r):
    rand_pos = randint(l,r)
    swap(arr, l, rand_pos)

    return [arr[l], arr]

def partition(arr, l, r):
    [p, arr] = pick_random(arr, l, r)

    i = l + 1

    for j in range(l+1, r+1):
        if arr[j] < p:
            swap(arr, i, j)
            
            i += 1
    
    swap(arr, l, i-1)

    return [i-1, arr]

def quick_sort(arr, l, r, num_comparisons):
    if r-l >= 1:
        num_comparisons += (r-l)
        [pivot, arr] = partition(arr, l, r)

        [arr, num_comparisons] = quick_sort(arr, l, pivot-1, num_comparisons)
        [arr, num_comparisons] = quick_sort(arr, pivot+1, r, num_comparisons)
    
    return [arr, num_comparisons]