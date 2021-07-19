values = []
weights = []
A = []

with open("knap_sack_big.txt") as a_file:
    for line in a_file:
        [value, weight] = [int(x) for x in line.strip().split()]
        values.append(value)
        weights.append(weight)

[capacity, num_items] = [values[0], weights[0]]
values = values[1:]
weights = weights[1:]

A = [([0] * (capacity+1)) for i in range(num_items+1)]

for i in range(1, num_items+1):
    for x in range(0, capacity+1):
        wi = weights[i-1] # weight of current item
        vi = values[i-1] # value of current item

        if wi <= x:
            A[i][x] = max(A[i-1][x], A[i-1][x - wi] + vi)
        else:
            A[i][x] = A[i-1][x]

print(A[num_items][capacity])