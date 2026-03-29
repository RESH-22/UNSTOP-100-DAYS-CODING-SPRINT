def count_consistent_cars(components, n, models):
    allowed = set(components)
    count = 0

    for model in models:
        valid = True
        for c in model:
            if c not in allowed:
                valid = False
                break
        if valid:
            count += 1

    return count


if __name__ == '__main__':
    components = input().strip()
    n = int(input().strip())
    models = input().split()   # models given in one line
    
    result = count_consistent_cars(components, n, models)
    print(result)
