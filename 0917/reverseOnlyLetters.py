def reverseOnlyLetters(self, S):
    l, r = 0, len(S) - 1
    res = list(S)
    while l < r:
        while l < r and not S[l].isalpha(): l += 1
        while l < r and not S[r].isalpha(): r -= 1
        res[l], res[r] = res[r], res[l]
        l, r = l+1, r-1
    return ''.join(res)