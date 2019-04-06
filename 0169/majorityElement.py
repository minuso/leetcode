def majorityElement(self, nums: List[int]) -> int:
    res, count = 0, 0 # Boyer–Moore majority vote algorithm
    for n in nums:
        if n == res:
            count += 1
        elif count != 0:
            count -= 1
        else:
            res, count = n, 1
    return res