def smallest_prime(n):
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n

def user_logic(n):
    if n % 2 == 0:
        return n // 2
    
    sp = smallest_prime(n)
    
    if sp == n:   # n is prime
        return 1
    
    n -= sp
    return 1 + (n // 2)

n = int(input())
result = user_logic(n)
print(result)
