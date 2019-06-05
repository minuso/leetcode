def toHex(self, num: int) -> str:
    if num == 0: return '0'
        
    HEX_BITS = '0123456789abcdef'
    if num < 0:
        num &= 0xFFFFFFFF
            
    rev = ''
    while num:
        rev += HEX_BITS[num % len(HEX_BITS)]
        num >>= 4
    return rev[::-1]