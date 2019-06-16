def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    f, end = [False]*(len(s) + 1), len(s)
    f[-1] = True
    while end > 0:
        if f[end]:
            for w in wordDict:
                start = end - len(w)
                if s[start:end] == w:
                    f[start] = True
        end -= 1
    return f[0]