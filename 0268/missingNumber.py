def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    exp_sum = (1 + n)*n//2
    return exp_sum - sum(nums)