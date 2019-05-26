def findLHS(self, nums: List[int]) -> int:
    res = 0
    freq = collections.Counter(nums)
    for n in freq:
        if n+1 in freq:
            res = max(res, freq[n] + freq[n+1])
    return res