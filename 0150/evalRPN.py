def evalRPN(self, tokens: List[str]) -> int:
    COMPUTATION = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a*b,
        '/': lambda a, b: int(a/b)
    }
        
    stack = []
    for t in tokens:
        if t not in COMPUTATION.keys():
            stack.append(int(t))
        else:
            b, a = stack.pop(), stack.pop() # order is important!
            stack.append(COMPUTATION[t](a, b))
    return stack[0]