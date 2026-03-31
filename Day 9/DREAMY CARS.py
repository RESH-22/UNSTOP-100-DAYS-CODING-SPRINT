def calculate_f_score(features, N):
    if N % 2 == 0:
        return 0
    
    result = 0
    for i in range(0, N, 2):
        result ^= features[i]
        
    return result


if __name__ == "__main__":
    N = int(input())
    features = list(map(int, input().split()))
    
    print(calculate_f_score(features, N))
