def letterCombinations(digits):
    if not digits:
        return []
    
    # Mapping of digits to letters
    keypad = {
        '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    # Backtracking function
    def backtrack(index, path):
        # If combination is complete
        if index == len(digits):
            result.append(path)
            return
        
        # Get letters for current digit
        letters = keypad[digits[index]]
        
        for ch in letters:
            backtrack(index + 1, path + ch)
    
    backtrack(0, "")
    
    # Return sorted result
    return sorted(result)


if __name__ == '__main__':
    digits = input().strip()
    res = letterCombinations(digits)
    print(" ".join(res))
