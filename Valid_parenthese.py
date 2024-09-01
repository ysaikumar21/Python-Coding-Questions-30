def is_valid_parenthese(expression):
    stack=[]
    pairs={')':'(',']':'[','}':'{'}
    for char in expression:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack
expression="()[]{}"
if is_valid_parenthese(expression):
    print("Valid parenthese")
else:
    print("Invalid parenthese")