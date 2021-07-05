from random import randint

def swap(arr, first, last):
    temp = arr[first]
    arr[first] = arr[last]
    arr[last] = temp

def pick_random_pivot(arr, l, r):
    rand_pos = randint(l,r)
    swap(arr, l, rand_pos)

    return [arr[l], arr]

def partition(arr, l, r):
    [p, arr] = pick_random_pivot(arr, l, r)

    i = l + 1

    for j in range(l+1, r+1):
        if arr[j] < p:
            swap(arr, i, j)
            
            i += 1
    
    swap(arr, l, i-1)

    return [i-1, arr]

# returns the ith order statistic in any given array, sorted or unsorted
def RSelect(arr, l, r, order_statistic):
    if len(arr) == 1:
        return arr[0]
    else:
        [pivot_place, arr] = partition(arr, l, r)

        if pivot_place == order_statistic-1:
            return arr[pivot_place]
        elif pivot_place > order_statistic-1:
            return RSelect(arr, l, pivot_place-1, order_statistic)
        else:
            return RSelect(arr, pivot_place+1, r, order_statistic)

def RSelectStarter(arr, order_statistic):
    return RSelect(arr, 0, len(arr)-1, order_statistic)