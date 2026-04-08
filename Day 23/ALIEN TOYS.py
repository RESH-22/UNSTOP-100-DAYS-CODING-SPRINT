def rearrange_blocks_to_form_name(S, P):
    n, m = len(S), len(P)
    
    if m > n:
        return 0, []
    
    # frequency arrays
    count_p = [0] * 26
    count_s = [0] * 26
    
    # fill pattern frequency
    for ch in P:
        count_p[ord(ch) - ord('a')] += 1
    
    result = []
    
    # sliding window
    for i in range(n):
        # add current char
        count_s[ord(S[i]) - ord('a')] += 1
        
        # remove left char if window > m
        if i >= m:
            count_s[ord(S[i - m]) - ord('a')] -= 1
        
        # check match
        if count_s == count_p:
            result.append(i - m + 2)  # 1-based index
    
    return len(result), result


# ---------- DRIVER CODE ----------
S = input().strip()
P = input().strip()

count, indices = rearrange_blocks_to_form_name(S, P)

if count == 0:
    print("none")
else:
    print(count)
    print(*indices)
