def findLengthOfLCIS(self, nums: List[int]) -> int:
    if not nums: return 0
    nums.append(nums[-1] - 1) # cut tail
        
    res, cur_len = 0, 1
    pre_num = nums[0] + 1 # cut head
    for n in nums:
        (res, cur_len) = (res, cur_len+1) if pre_num < n else (max(res, cur_len), 1)
        pre_num = n
    return res