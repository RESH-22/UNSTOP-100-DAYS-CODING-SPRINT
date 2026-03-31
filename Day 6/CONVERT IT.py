def modify_array(n, arr):
    max_so_far = 0
    result = []

    for i in range(n):
        max_so_far = max(max_so_far, arr[i])
        result.append(arr[i] + max_so_far)

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))

    modified_arr = modify_array(n, arr)

    print(" ".join(map(str, modified_arr)))


if __name__ == "__main__":
    main()
