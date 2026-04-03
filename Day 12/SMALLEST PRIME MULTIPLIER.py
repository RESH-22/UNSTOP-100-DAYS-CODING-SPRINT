import math

def compute_x(p, n):
    """
    Write your logic here.
    Parameters:
        p (int): First integer
        n (int): Second integer
    Returns:
        int: Smallest number divisible by both p and n
    """
    return (p * n) // math.gcd(p, n)


p, n = map(int, input().split())
print(compute_x(p, n))
