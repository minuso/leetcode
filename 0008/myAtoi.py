def myAtoi(self, str: str) -> int:
    tmp = str.lstrip()
    if not tmp: return 0
    if tmp[0] not in '+-0123456789': return 0
        
    INT_MAX, INT_MIN = (1 << 31) - 1, -(1 << 31)
        
    sign = -1 if tmp[0] == '-' else 1
    scalar = ''
    i = 1 if tmp[0] in '+-' else 0
    while i < len(tmp) and tmp[i].isdigit(): 
        scalar += tmp[i]
        i += 1
        
    if not scalar: return 0
        
    res = sign*int(scalar)
    if res > INT_MAX: return INT_MAX
    if res < INT_MIN: return INT_MIN
    return res