def searchInsert(self, nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:               # when l = r and not found
        m = (l + r)//2
        if nums[m] < target: 
            l = m + 1           # this helps l to be an insert position
        elif nums[m] > target: 
            r = m - 1
        else:
            return m
    return l