def frequencySort(self, s: str) -> str:
    c_cnts = collections.Counter(s).most_common()
    return ''.join(c*cnt for c, cnt in c_cnts)