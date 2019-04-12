def reverseStr(self, s, k):
    res = ''
    for i in range(0, len(s), k):
        if (i/k)%2:
            res += s[i:i+k]
        else:
            res += s[i:i+k][::-1]
    return res