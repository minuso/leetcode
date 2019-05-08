def singleNumber(self, nums):
    diff_bit = reduce(operator.xor, nums) # result in xor of two target numbers
    diff_bit &= -diff_bit # get a different bit between two target numbers
        
    res = [0, 0]
    for n in nums:
        res[n & diff_bit > 0] ^= n # use this bit to separate target numbers
    return res