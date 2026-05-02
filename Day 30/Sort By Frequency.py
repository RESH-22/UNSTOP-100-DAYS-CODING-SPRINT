s = input()

from collections import Counter, OrderedDict

count = Counter(s)

# Track first occurrence index for tie-breaking
first_seen = {}
for i, ch in enumerate(s):
    if ch not in first_seen:
        first_seen[ch] = i

# Sort: primary = frequency descending, secondary = first occurrence ascending
sorted_chars = sorted(count.keys(), key=lambda c: (-count[c], first_seen[c]))

print(''.join(c * count[c] for c in sorted_chars))
