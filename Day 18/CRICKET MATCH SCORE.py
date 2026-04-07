import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

target = n - 1

if target == 0:
    print("true")
else:
    max_reach = 0
    for i in range(n):
        if i > max_reach:
            # stuck, can't proceed
            print("false")
            break
        max_reach = max(max_reach, i + arr[i])
        if max_reach >= target:
            print("true")
            break
    else:
        print("false" if max_reach < target else "true")
