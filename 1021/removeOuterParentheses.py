def removeOuterParentheses(self, S: str) -> str:
    res, lcount = '', 0
    for c in S:
        if lcount == 0 or (lcount == 1 and c == ')'):
            lcount ^= 1
            continue
        lcount += 1 if c == '(' else -1
        res += c
    return res