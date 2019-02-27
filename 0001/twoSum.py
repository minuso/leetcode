def twoSum(self, nums, target):
    cand = {} # store candidate value with corresponding index
    for i, n in enumerate(nums):
        if n in cand:
            return [cand[n], i]
        cand[target - n] = i # candidate value is 'target - n'