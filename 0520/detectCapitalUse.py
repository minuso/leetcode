def detectCapitalUse(self, word: str) -> bool:
    if word.isupper(): return True
        
    for c in word[1:]:
        if c.isupper():
            return False
    return True