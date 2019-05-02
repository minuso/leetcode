def toGoatLatin(self, S: str) -> str:
    ws, mas = S.split(' '), 'ma'
    for i, w in enumerate(ws):
        if w[0] not in 'aeiouAEIOU':
            ws[i] = ws[i][1:] + w[0]
        mas += 'a'
        ws[i] += mas
    return ' '.join(ws)