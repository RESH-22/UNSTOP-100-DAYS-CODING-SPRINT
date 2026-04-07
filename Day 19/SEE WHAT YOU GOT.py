def user_logic(A, B, C):
    return A ^ (B & C)


# ---- Input Handling ----
T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    print(user_logic(A, B, C))
