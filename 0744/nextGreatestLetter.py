def nextGreatestLetter(self, letters, target):
    if target >= letters[-1]: return letters[0]
        
    l, r = 0, len(letters) - 1
    while l < r:
        m = (l + r) >> 1
        if letters[m] > target:
            r = m
        else:
            l = m + 1
    return letters[l]