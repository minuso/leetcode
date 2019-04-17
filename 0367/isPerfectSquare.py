def isPerfectSquare(self, num: int) -> bool:
    if num == 1 or num == 4: return True
        
    l, r = 1, num // 2
    while l < r:
        m = (l + r) // 2
        mul = m*m
        if mul > num:
            r = m - 1
        elif mul < num:
            l = m + 1
        else:
            return True
    return r*r == num