def removeElement(self, nums, val):
    i = 0
    while i < len(nums):
        if nums[i] != val:
            i += 1
        else:
            del nums[i]
    return len(nums)