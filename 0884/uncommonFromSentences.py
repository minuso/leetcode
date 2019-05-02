def uncommonFromSentences(self, A: str, B: str) -> List[str]:
    ws = {}
    for w in (A + ' ' + B).split(' '):
        if w in ws:
            ws[w] += 1
        else:
            ws[w] = 1
    return [w for w in ws if ws[w] == 1]