# Input - sizes on line 1, list1 on line 2, list2 on line 3
sizes = list(map(int, input().split()))
n1, n2 = sizes[0], sizes[1]

vals1 = list(map(int, input().split()))
vals2 = list(map(int, input().split()))

# Find longest common suffix by matching from the end
i, j = len(vals1) - 1, len(vals2) - 1
common_start = -1

while i >= 0 and j >= 0:
    if vals1[i] == vals2[j]:
        common_start = vals1[i]
        i -= 1
        j -= 1
    else:
        break

print(common_start)
