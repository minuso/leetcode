def commonChars(self, A: List[str]) -> List[str]:
    res = []
    for c in string.ascii_lowercase:
        counts = [s.count(c) for s in A] # str.count(char) usage
        res += [c]*min(counts)
    return res