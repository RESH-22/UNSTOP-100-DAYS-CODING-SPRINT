def find_flower_indices(n, t, arr):
    left = 0
    right = n - 1

    while left < right:
        s = arr[left] + arr[right]

        if s == t:
            return (left, right)
        elif s < t:
            left += 1
        else:
            right -= 1

def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))

    n = data[0]
    t = data[1]
    arr = data[2:]

    i, j = find_flower_indices(n, t, arr)
    print(i, j)

if __name__ == "__main__":
    main()
