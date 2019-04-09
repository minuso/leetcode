def permute(self, nums: List[int]) -> List[List[int]]:
    if len(nums) == 1: return [nums]
        
    res = []
    for i, n in enumerate(nums):
        for p in self.permute(nums[:i] + nums[i+1:]): # dfs
            res.append([n] + p)
    return res