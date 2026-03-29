def transform_string(s, ch):
    # Find last occurrence of ch
    idx = s.rfind(ch)
    
    # If character not found, return original string
    if idx == -1:
        return s
    
    # Reverse substring from idx to end
    return s[:idx] + s[idx:][::-1]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    s = data[0]  # First input is the string s
    ch = data[1]  # Second input is the character ch
    
    # Call user logic function and print the output
    transformed_string = transform_string(s, ch)
    print(transformed_string)

if __name__ == "__main__":
    main()
