def check_if_can_break(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    s1_break_s2 = True
    s2_break_s1 = True

    for i in range(len(s1)):
        if s1[i] < s2[i]:
            s1_break_s2 = False
        if s2[i] < s1[i]:
            s2_break_s1 = False

    return s1_break_s2 or s2_break_s1


s1 = input().strip()
s2 = input().strip()

result = check_if_can_break(s1, s2)

if result:
    print("true")
else:
    print("false")
