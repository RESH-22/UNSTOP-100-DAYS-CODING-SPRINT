s = input()
result = []
i = 0
while i < len(s):
    if s[i] == 'S':
        result.append('send')
        i += 1
    elif s[i:i+5] == '[sps]':
        result.append('ships')
        i += 5
    elif s[i:i+2] == '[]':
        result.append('the')
        i += 2
    else:
        i += 1

print(' '.join(result))
