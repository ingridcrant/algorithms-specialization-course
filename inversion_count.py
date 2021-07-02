# number of inversions in a given array
def num_inversions(arr):
    return sort_and_count(arr, 0)[1]

def sort_and_count(A, inversion_count):
    n = len(A)

    if n == 1:
        return [A, inversion_count]
    else:
        half = (n+1)//2
        [B, x] = sort_and_count(A[:half], inversion_count)
        [C, y] = sort_and_count(A[half:], inversion_count)
        [D, z] = merge_and_countSplitInv(B, C)

        return [D, x+y+z]

def merge_and_countSplitInv(B, C):
    i = 0
    j = 0

    inversion_count = 0
    len_B, len_C = len(B), len(C)
    D = []

    for k in range(len_B + len_C):
        if i < len(B) and j < len(C):
            if B[i] <= C[j]:
                D.append(B[i])
                i += 1
            else:
                D.append(C[j])
                inversion_count += len_B - i
                j += 1
        else:
            if i == len(B):
                D += C[j:]
            else:
                D += B[i:]
            break
    
    return [D, inversion_count]

arr = [1, 20, 6, 4, 5]
result = num_inversions(arr)
print("Number of inversions are", result)