class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int: # reservoir sampling
        res, cnt = -1, 0        
        for i, v in enumerate(self.nums):
            if self.nums[i] == target:
                cnt += 1
                if random.randint(1, cnt) == cnt:
                    res = i
        return res