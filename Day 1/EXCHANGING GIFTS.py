def find_youngest_member(n, m, gifts):
    # Edge case: if n == 1, that single member is youngest
    if n == 1:
        return 1

    # Initialize in-degree and out-degree arrays
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    # Process gift exchanges
    for a, b in gifts:
        out_degree[a] += 1
        in_degree[b] += 1

    # Find member who receives from everyone and gives to no one
    for i in range(1, n + 1):
        if in_degree[i] == n - 1 and out_degree[i] == 0:
            return i

    return -1


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of family members
    m = int(data[1])  # Number of gifts exchanged
    
    gifts = []
    index = 2
    for _ in range(m):
        a_i = int(data[index])
        b_i = int(data[index + 1])
        gifts.append((a_i, b_i))
        index += 2
    
    # Call user logic function and print the output
    result = find_youngest_member(n, m, gifts)
    print(result)

if __name__ == "__main__":
    main()
