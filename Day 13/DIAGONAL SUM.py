def diagonal_sum(matrix, n):
    if n % 2 == 0:
        return 2 * n
    else:
        return 2 * n - 1

if __name__ == '__main__':
    n = int(input())
    result = diagonal_sum([], n)
    print(result)
