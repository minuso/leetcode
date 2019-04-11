def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1]*len(nums)
    for i in range(1, len(nums)):
        res[i] = res[i-1]*nums[i-1] # record step product from left to right
    tmp = 1
    for i in range(len(nums) - 2, -1, -1):
        tmp *= nums[i+1]            # record step product from right to left
        res[i] *= tmp               # left * right
    return res