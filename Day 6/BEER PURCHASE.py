def max_bottle_cost(n, x, costs):
    costs.sort()
    
    prefix = [0]*n
    prefix[0] = costs[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + costs[i]

    total = 0

    for k in range(n):
        if prefix[k] > x:
            break

        # max days we can buy k+1 bottles
        days = (x - prefix[k]) // (k+1) + 1
        total += days

    return total


def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    n = data[0]
    x = data[1]
    costs = data[2:]

    print(max_bottle_cost(n, x, costs))


if __name__ == "__main__":
    main()
