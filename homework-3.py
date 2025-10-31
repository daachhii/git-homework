def DictonaryFunction(text):
    result = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            result[char] = result.get(char, 0) + 1
    return result

print(DictonaryFunction("hello"))
