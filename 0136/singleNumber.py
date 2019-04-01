def singleNumber(self, nums):
    res = 0
    for n in nums:
        res ^= n # doing xor on every even-count numbers results 0
    return res