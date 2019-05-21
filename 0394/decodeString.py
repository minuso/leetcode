def decodeString(self, s: str) -> str:
    stack = []
    nxt_k, cur_str = 0, ''
    for c in s:
        if c.isdigit():
            nxt_k = nxt_k*10 + int(c)
        elif c.isalpha():
            cur_str += c
        elif c == '[':
            stack.append((nxt_k, cur_str))
            nxt_k, cur_str = 0, ''
        elif c == ']':
            cur_k, pre_str = stack.pop()
            cur_str = pre_str + cur_k*cur_str
    return cur_str