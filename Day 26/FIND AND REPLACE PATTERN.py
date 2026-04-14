def findAndReplacePattern(words, pattern):
    def match(word):
        forward = {}
        reverse = {}
        
        for w, p in zip(word, pattern):
            # if mapping of forward not same as reverse, permutation not found
            if w not in forward: 
                forward[w] = p
            if p not in reverse: 
                reverse[p] = w
            if(forward[w], reverse[p]) != (p, w):
                return False
        return True
        
    return list(filter(match, words))

n = int(input())
words = [s for s in input().split()]
pattern = input()
result = findAndReplacePattern(words, pattern)

# Display results to user
print(len(result))
for ans in result:
    print(ans, end = ' ')
