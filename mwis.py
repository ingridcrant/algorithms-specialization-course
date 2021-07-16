from math import inf

weights = []

with open("mwis.txt") as a_file:
    for line in a_file:
        weights.append(int(line.strip()))

n = weights[0]
weights = [0] + weights[1:]

max_weights_IS = [-inf] * (n+1)
max_weights_IS[0] = 0
max_weights_IS[1] = weights[1]

for i in range(2, n+1):
    max_weights_IS[i] = max(max_weights_IS[i-1], max_weights_IS[i-2] + weights[i])

i = n
S = set()
vertices = [1, 2, 3, 4, 17, 117, 517, 997]
final_str = ""

while i >= 1:
    if max_weights_IS[i-1] >= (max_weights_IS[i-2] + weights[i]):
        i -= 1
    else:
        S.add(i)
        i -= 2

for vertex in vertices:
    if vertex in S:
        final_str += "1"
    else:
        final_str += "0"

print(final_str)
