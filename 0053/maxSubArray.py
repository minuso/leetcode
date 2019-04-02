def maxSubArray(self, nums):
    max_cur = max_sum = nums[0]
    for n in nums[1:]:
        max_cur = max(max_cur + n, n) # extend or new a subarray (local)
        max_sum = max(max_sum, max_cur) 
    return max_sum