def findErrorNums(self, nums: List[int]) -> List[int]:
    def findDup(nums):
        contain = [False]*len(nums)
        for n in nums:
            if contain[n-1]:
                return n
            contain[n-1] = True
        
    dup = findDup(nums)
    d =  (1 + len(nums))*len(nums)//2 - sum(nums)
    return [dup, dup+d]