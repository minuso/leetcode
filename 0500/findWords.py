def findWords(self, words: List[str]) -> List[str]:
    CH_ROW = '12210111011122000010020202'
    CH_BASE = ord('a')
        
    res = []
    for w in words:
        r, same_row = CH_ROW[ord(w[0].lower()) - CH_BASE], True
        for c in w[1:]:
            if CH_ROW[ord(c.lower()) - CH_BASE] != r:
                same_row = False
                break
        if same_row:
            res.append(w)
    return res