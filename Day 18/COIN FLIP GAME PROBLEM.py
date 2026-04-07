import math

def find(m):
    return int(math.isqrt(m))  # integer sqrt


if __name__ == "__main__":
    m = int(input())
    print(find(m))
