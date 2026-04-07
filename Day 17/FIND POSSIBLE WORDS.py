def count_characters(words, chars):
    from collections import Counter
    
    char_count = Counter(chars)
    total_length = 0
    
    for word in words:
        word_count = Counter(word)
        
        for ch in word_count:
            if word_count[ch] > char_count.get(ch, 0):
                break
        else:
            total_length += len(word)
    
    return total_length


# 🔥 Input handling (IMPORTANT FIX)
n = int(input())
words = []

for _ in range(n):
    words.append(input().strip())

chars = input().strip()

print(count_characters(words, chars))
