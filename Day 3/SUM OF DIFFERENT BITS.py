def compareBits(a, b):
    n = len(a)
    m = len(b)

    # prefix count of '1's in b
    prefix = [0] * (m + 1)
    for i in range(m):
        prefix[i+1] = prefix[i] + (b[i] == '1')

    total = 0

    for i in range(n):
        l = i
        r = i + (m - n)

        ones = prefix[r+1] - prefix[l]
        length = r - l + 1
        zeros = length - ones

        if a[i] == '1':
            total += zeros
        else:
            total += ones

    return total


if __name__ == '__main__':
    a = input().strip()
    b = input().strip()
    print(compareBits(a, b))
