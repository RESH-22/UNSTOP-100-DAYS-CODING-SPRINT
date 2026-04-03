def determine_winner(N, smit_str, joy_str):
    smit_unique = len(set(smit_str))
    joy_unique = len(set(joy_str))
    
    if smit_unique > joy_unique:
        return "SMIT"
    elif joy_unique > smit_unique:
        return "JOY"
    else:
        return "TIE"


N = int(input())
smit_str = input().strip()
joy_str = input().strip()

print(determine_winner(N, smit_str, joy_str))
