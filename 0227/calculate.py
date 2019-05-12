def calculate(self, s):
    s += 'E' # end flag to hit the last computation
    stack, num, pre_op = [], 0, '+'
    for c in s:
        if c.isdigit(): num = num*10 + int(c)
        elif not c.isspace():
            if   pre_op == '-': stack.append(-num)
            elif pre_op == '+': stack.append(num)
            elif pre_op == '*': stack.append(stack.pop()*num)
            elif pre_op == '/': stack.append(int(stack.pop()/float(num))) # cases like '-3/2' should be -1, not -2
            pre_op, num = c, 0
    return sum(stack)