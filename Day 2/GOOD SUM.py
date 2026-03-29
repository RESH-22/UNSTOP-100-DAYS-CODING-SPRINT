def good_sum(N, A):
    stack = []

    for x in A:
        if x >= 0:
            stack.append(x)
        else:
            target = abs(x)
            removed_sum = 0

            while stack and removed_sum < target:
                removed_sum += stack.pop()

            stack.append(target)

    return sum(stack)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the integer N
    A = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and print the output
    result = good_sum(N, A)
    print(result)

if __name__ == "__main__":
    main()
