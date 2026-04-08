def specialmsg(s, vocab):
    # Step 1: build dictionary
    mp = {}
    for key, val in vocab:
        mp[key] = val

    result = []
    i = 0
    n = len(s)

    while i < n:
        if s[i] == '(':
            j = i + 1
            
            # find closing bracket
            while j < n and s[j] != ')':
                j += 1
            
            key = s[i + 1:j]  # extract inside
            
            # replace
            if key in mp:
                result.append(mp[key])
            else:
                result.append("?")
            
            i = j + 1  # move after ')'
        
        else:
            result.append(s[i])
            i += 1

    return "".join(result)


# ---------- DRIVER CODE ----------
s = input().strip()
n = int(input())

vocab = []
for _ in range(n):
    key, val = input().split()
    vocab.append([key, val])

print(specialmsg(s, vocab))
