def countSmaller(self, nums: List[int]) -> List[int]:
    res_rev, sort_arr = [], []
    for n in reversed(nums):
        i = bisect.bisect_left(sort_arr, n)
        res_rev.append(i) # index means the number of smaller elements too
        sort_arr.insert(i, n)
    return res_rev[::-1]