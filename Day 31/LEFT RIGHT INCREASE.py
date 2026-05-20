import sys
input = sys.stdin.readline

def solve():
    line1 = input().split()
    N, P = int(line1[0]), int(line1[1])
    A = list(map(int, input().split()))
    
    initial_sum = sum(A)
    
    current = A[:]
    
    for day in range(P):
        # Find which elements are non-zero (they spread)
        new = current[:]
        for i in range(N):
            if current[i] != 0:
                if i > 0:
                    new[i-1] += 2
                if i < N-1:
                    new[i+1] += 2
        current = new
    
    final_sum = sum(current)
    print(final_sum - initial_sum)

solve()
