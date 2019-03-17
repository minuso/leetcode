def isValid(self, s):
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
        
    stack = []
    for c in s:
        if c in brackets:               # when meeting a open bracket
            stack.append(brackets[c])   # push corresponding close bracket
            continue                    # and wait for matching
        if not stack or c != stack.pop():
            return False
        
    if stack: return False # some brackets are remainded
    return True