def findAnagrams(self, s: str, p: str) -> List[int]:
    if len(s) < len(p): return []
        
    dict_p = dict.fromkeys(string.ascii_lowercase, 0)
    dict_s = dict.fromkeys(string.ascii_lowercase, 0)
    for i, c in enumerate(p):
        dict_p[c] += 1
        dict_s[s[i]] += 1
        
    res = [] if dict_s != dict_p else [0]
    for i in range(len(p), len(s)):
        cur_h, nxt_t = s[i - len(p)], s[i]
        dict_s[cur_h] -= 1
        dict_s[nxt_t] += 1
        if dict_s == dict_p:
            res.append(i - len(p) + 1)
    return res