def modify_string(n, s):
    primes = {2, 3, 5, 7}
    prime_list = []

    # collect prime digits
    for ch in s:
        if ch.isdigit():
            num = int(ch)
            if num in primes:
                prime_list.append(num)

    # compute unique number
    if prime_list:
        unique = sum(prime_list) // len(prime_list)
    else:
        unique = None

    result = []

    for ch in s:
        if ch.isdigit():
            num = int(ch)

            if unique is None:  # no primes
                index = num
            else:
                index = num % unique

            result.append(chr(ord('a') + index))
        else:
            result.append(ch)

    return "".join(result)


n = int(input())
s = input().strip()

print(modify_string(n, s))
