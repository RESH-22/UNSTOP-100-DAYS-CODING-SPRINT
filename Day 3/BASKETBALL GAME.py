def user_logic(ops):
    stack = []

    for op in ops:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))

    return sum(stack)


if __name__ == "__main__":
    n = int(input().strip())
    ops = input().split()   # FIX: read operations in one line

    result = user_logic(ops)
    print(result)
