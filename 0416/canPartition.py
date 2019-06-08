def canPartition(self, nums):
    num_sum = sum(nums)
    if num_sum & 1: return False
        
    d = {0: True} # store target-canFind pairs
    def canFindSum(target, idx):
        if target in d: return d[target] 
            
        d[target] = False
        if target > 0:
            for i in range(idx, len(nums)):
                if canFindSum(target - nums[i], i+1):
                    d[target] = True
                    break
        return d[target]
        
    return canFindSum(num_sum//2, 0)