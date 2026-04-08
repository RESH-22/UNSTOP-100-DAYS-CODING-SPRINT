MOD = 10**9 + 7

def power(base, exp):
    result = 1
    base %= MOD
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % MOD
        base = (base * base) % MOD
        exp //= 2
    
    return result


def calculate_valid_pins(n):
    even_count = (n + 1) // 2
    odd_count = n // 2
    
    return (power(5, even_count) * power(4, odd_count)) % MOD


if __name__ == "__main__":
    n = int(input().strip())
    print(calculate_valid_pins(n))
