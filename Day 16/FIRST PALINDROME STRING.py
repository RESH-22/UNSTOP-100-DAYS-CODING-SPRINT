n = int(input())
words = input().split()

result = ""
for word in words:
    if word == word[::-1]:
        result = word
        break

print(result)
