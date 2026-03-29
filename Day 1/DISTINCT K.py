# Read input
n = int(input().strip())

strings = []
for _ in range(n):
    strings.append(input().strip())

k = int(input().strip())

# Count frequency of each string
freq = {}

for s in strings:
    freq[s] = freq.get(s, 0) + 1

# Collect distinct strings in order of appearance
distinct = []

for s in strings:
    if freq[s] == 1:
        distinct.append(s)

# Output result
if k <= len(distinct):
    print(distinct[k - 1])
else:
    print(-1)
