def merge_sort(weight_to_length):
    if len(weight_to_length) > 1:
        half = len(weight_to_length)//2

        a = merge_sort(weight_to_length[:half])
        b = merge_sort(weight_to_length[half:])

        i = 0
        j = 0

        for k in range(len(weight_to_length)):
            if i < len(a) and j < len(b):
                if (a[i][0]/a[i][1]) < (b[j][0]/b[j][1]):
                    weight_to_length[k] = a[i]
                    i += 1
                elif (a[i][0]/a[i][1]) > (b[j][0]/b[j][1]):
                    weight_to_length[k] = b[j]
                    j += 1
                else:
                    if a[i][0] > b[j][0]:
                        weight_to_length[k] = b[j]
                        j += 1
                    elif a[i][0] < b[j][0]:
                        weight_to_length[k] = a[i]
                        i += 1
                    else:
                        weight_to_length[k] = b[j]
                        j += 1
            else:
                if i == len(a):
                    weight_to_length = weight_to_length[:k] + b[j:]
                else:
                    weight_to_length = weight_to_length[:k] + a[i:]
                break
    
    # base case: size of nums is 1
    return weight_to_length

def compute_completion_times(weight_to_length):
    c = 0
    sum = 0
    for pair in weight_to_length:
        weight = pair[0]
        length = pair[1]
        c += length

        sum += weight * c
    
    return sum

weight_to_length = []

with open("jobs.txt") as a_file:
    line_num = 0
    for line in a_file:
        line_num += 1
        if line_num > 1:
            weight_to_length.append([int(x) for x in line.strip().split(" ")])

weight_to_length = merge_sort(weight_to_length)
print(compute_completion_times(weight_to_length[::-1]))