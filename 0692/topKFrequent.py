def topKFrequent(self, words: List[str], k: int) -> List[str]:
    freq = collections.Counter(words)
    group = {}
    for w in freq:
        if freq[w] in group: group[freq[w]].append(w)
        else: group[freq[w]] = [w]
                
    res = []
    for f in sorted(group, reverse=True):
        res += sorted(group[f])
        if len(res) >= k:
            break
    return res[:k]