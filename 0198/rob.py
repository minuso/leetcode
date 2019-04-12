def rob(self, nums: List[int]) -> int:
    last, now = 0, 0
    for n in nums: 
        last, now = now, max(last + n, now)
    return now