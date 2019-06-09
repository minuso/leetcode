def repeatedSubstringPattern(self, s: str) -> bool:
    # If True, s has as least 2 repeated substrings
    # S = s*2 # has at least 4 repeated substrings
    # S[1:-1] remove the first and the last substring,
    # which has at least 2 repeated substrings (contains s)
    return s in (s*2)[1:-1]