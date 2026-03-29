import sys
data = sys.stdin.read().strip().split()

t = int(data[0])
index = 1
result = []

for _ in range(t):
    n = int(data[index])
    index += 1
    s = data[index]
    index += 1
    
    possible = True
    
    segments = s.split('W')
    
    for seg in segments:
        if len(seg) == 0:
            continue
        
        if 'R' not in seg or 'B' not in seg:
            possible = False
            break
    
    result.append("YES" if possible else "NO")

print("\n".join(result))
