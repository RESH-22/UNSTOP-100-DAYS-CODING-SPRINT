def find_largest_pack(N):
    p = 1
    while p * 2 <= N:
        p *= 2
    return p


N = int(input())
print(find_largest_pack(N))
