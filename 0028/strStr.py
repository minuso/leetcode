def strStr(self, haystack, needle):
    if not needle: return 0
        
    len_str = len(needle)
    for idx in range(len(haystack) - len_str + 1):
        if haystack[idx] != needle[0]: continue # check the necessary for slicing (a slow process)
        if haystack[idx:idx+len_str] == needle:
            return idx
    return -1