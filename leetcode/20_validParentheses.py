# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Input: s = "{[]}"
# Output: true
#
# Input: s = "()[]{}"
# Output: true
#
# Input: s = "([)]"
# Output: false
#
# Input: s = "(]"
# Output: false

def isValid(s):
    stack = []
    d = {')':'(', ']':'[', '}':'{'}

    for char in s:
        if char in d.values():
            stack.append(char)
        elif char in d.keys():
            if stack == [] or d[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

userInput = input("Please enter parentheses: ")
result =isValid(userInput)
print(result)



