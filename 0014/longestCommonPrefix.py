def longestCommonPrefix(self, strs):
    if not strs: return ""
        
    lcp = strs[0]
    for s in strs[1:]:
        lcp = self.lcp_of_two_str(lcp, s)
    return lcp
    
def lcp_of_two_str(self, s1, s2):
    lcp = ""
    max_len = min(len(s1), len(s2))
    for i in range(max_len):
        if s1[i] != s2[i]:
            return lcp
        lcp += s1[i]
    return lcp