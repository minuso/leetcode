def isAnagram(self, s: str, t: str) -> bool:
    for c in set(s):
        if s.count(c) != t.count(c):
            return False
    return set(s) == set(t)