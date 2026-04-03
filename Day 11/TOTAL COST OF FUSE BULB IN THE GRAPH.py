def calculate_total_cost(k, n, m, graph):
    # handle corner case
    if m == 0:
        return 0
    
    # count bulbs divisible by m in range 1..n
    count = n // m
    
    # bulb 0 must not be counted
    if 0 % m == 0:
        pass  # already excluded since we start from 1
    
    return count * k


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    k = int(data[0])
    n = int(data[1])
    m = int(data[2])
    len_graph = int(data[3])

    graph = []
    idx = 4
    for _ in range(len_graph):
        u = int(data[idx])
        v = int(data[idx + 1])
        graph.append([u, v])
        idx += 2

    result = calculate_total_cost(k, n, m, graph)
    print(result)


if __name__ == "__main__":
    main()
