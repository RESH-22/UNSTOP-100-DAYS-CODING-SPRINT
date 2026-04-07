def min_additions(s):
    # Replace last character with 'c'
    s = s[:-1] + 'c'
    
    n = len(s)
    
    # KMP failure function approach
    # Concatenate s + '#' + reverse(s)
    rev = s[::-1]
    combined = s + '#' + rev
    
    # Build KMP failure/prefix table
    lps = [0] * len(combined)
    length = 0
    i = 1
    while i < len(combined):
        if combined[i] == combined[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    # lps[-1] = length of longest palindromic prefix
    return n - lps[-1]

s = input().strip()
print(min_additions(s))
