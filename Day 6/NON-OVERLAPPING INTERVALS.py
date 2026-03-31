def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            count += 1
        else:
            prev_end = intervals[i][1]

    return count


if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    N = data[0]
    M = data[1]
    
    intervals = []
    idx = 2
    
    for _ in range(N):
        start = data[idx]
        end = data[idx+1]
        intervals.append([start, end])
        idx += 2

    print(erase_overlap_intervals(intervals))
