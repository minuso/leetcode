def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    res, cur = 0, 0
    for b in nums:
        cur += b
        if b == 0:
            res = max(res, cur)
            cur = 0
    return max(res, cur)