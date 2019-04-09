def searchRange(self, nums: List[int], target: int) -> List[int]:
    if not nums: return [-1, -1]
        
    def bs(nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if nums[m] < target: l = m + 1 # search the first index
            else: r = m
        return l
        
    i = bs(nums, target)
    if nums[i] != target: return [-1, -1]
        
    d = bs(nums[i:], target + 1) # search next value to get the distance
    if nums[i+d] == target:
        return [i, i+d]
    return [i, i+d-1]