def backspaceCompare(self, S, T):
    def genList(string):
        res = []
        for c in string:
            if c == '#': 
                if res: res.pop()
            else: res.append(c)
        return res
        
    return genList(S) == genList(T)