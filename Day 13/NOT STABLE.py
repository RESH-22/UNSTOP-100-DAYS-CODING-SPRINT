def valid(seq):
    s = 0
    for x in seq:
        s += x
        if s == 0:
            return False
    return True

def user_logic(n, arr):

    asc = sorted(arr)
    desc = sorted(arr, reverse=True)

    asc_ok = valid(asc)
    desc_ok = valid(desc)

    if not asc_ok and not desc_ok:
        return ("IMPOSSIBLE", [])

    if asc_ok and desc_ok:
        if desc[0] > asc[0]:
            return ("POSSIBLE", desc)
        else:
            return ("POSSIBLE", asc)

    if asc_ok:
        return ("POSSIBLE", asc)

    return ("POSSIBLE", desc)


n = int(input())
arr = list(map(int, input().split()))

status, seq = user_logic(n, arr)

print(status)
if status == "POSSIBLE":
    print(*seq)
