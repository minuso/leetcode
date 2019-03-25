def findComplement(self, num: int) -> int:
    res = 1
    while res < num: # generate all-1 number with the same length of num (in binary)
        res <<= 1
        res += 1
    res ^= num # use xor to compute the complement
    return res