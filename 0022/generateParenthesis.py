def generateParenthesis(self, n):
    res = []
    def gen(s, lt, rt): # generate n left and n right parenthesis
        if len(s) == n*2:
            res.append(s)
            return
        if lt < n: 
            gen(s + '(', lt + 1, rt) # continuous left
        if rt < lt: 
            gen(s + ')', lt, rt + 1) # closed by right
        
    gen('', 0, 0)
    return res