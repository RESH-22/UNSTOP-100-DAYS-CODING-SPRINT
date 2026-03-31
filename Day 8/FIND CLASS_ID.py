import sys

def peakIndexInMountainArray(A):
    n = len(A)

    for i in range(n):
        left = A[i-1] if i > 0 else -1
        right = A[i+1] if i < n-1 else -1

        if A[i] >= left and A[i] >= right:
            return i

    return -1


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    print(peakIndexInMountainArray(arr))
