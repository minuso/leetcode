def findUnsortedSubarray(self, nums: List[int]) -> int:
    if len(nums) == 1: return 0
        
    l_err, pre = 0, nums[-1]
    for i, v in enumerate(reversed(nums)): # find leftmost unsorted index
        if pre < v:
            l_err = i
        else:
            pre = v
    l_err = len(nums) - 1 - l_err # convert to index
        
    r_err, pre = 0, nums[0]
    for i, v in enumerate(nums):           # find rightmost unsorted index
        if pre > v:
            r_err = i
        else:
            pre = v
    return max(0, r_err - l_err + 1)