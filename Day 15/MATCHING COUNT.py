def matching_count(items, ruleKey, ruleValue):
    count = 0
    key_index = {'type': 0, 'color': 1, 'name': 2}[ruleKey]

    for item in items:
        if item[key_index] == ruleValue:
            count += 1

    return count


def main():
    import sys

    # Read number of items
    n = int(sys.stdin.readline().strip())

    items = []
    for _ in range(n):
        # Read type, color, name
        item = sys.stdin.readline().strip().split()
        items.append(item)

    # Read ruleKey and ruleValue
    ruleKey = sys.stdin.readline().strip()
    ruleValue = sys.stdin.readline().strip()

    # Get result
    result = matching_count(items, ruleKey, ruleValue)

    # Print result
    print(result)


if __name__ == "__main__":
    main()
