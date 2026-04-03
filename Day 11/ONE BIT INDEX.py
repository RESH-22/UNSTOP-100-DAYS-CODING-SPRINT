def count_good_indices(n, arr):
    prefix_sum = 0
    count = 0

    for i in range(n):
        prefix_sum += arr[i]

        # check if prefix sum has exactly one bit set
        if prefix_sum > 0 and (prefix_sum & (prefix_sum - 1)) == 0:
            count += 1

    return count


n = int(input())
arr = list(map(int, input().split()))

print(count_good_indices(n, arr))
