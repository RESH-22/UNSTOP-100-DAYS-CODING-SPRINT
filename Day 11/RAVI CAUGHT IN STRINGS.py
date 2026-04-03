def longest_palindromic_substring_length(n, s):
    # Transform string
    t = "#" + "#".join(s) + "#"
    m = len(t)

    p = [0] * m
    center = 0
    right = 0
    max_len = 0

    for i in range(m):
        mirror = 2 * center - i

        if i < right:
            p[i] = min(right - i, p[mirror])

        # expand palindrome
        a = i + p[i] + 1
        b = i - p[i] - 1

        while a < m and b >= 0 and t[a] == t[b]:
            p[i] += 1
            a += 1
            b -= 1

        if i + p[i] > right:
            center = i
            right = i + p[i]

        max_len = max(max_len, p[i])

    return max_len


n = int(input())
s = input().strip()

print(longest_palindromic_substring_length(n, s))
