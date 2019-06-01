class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0]*len(nums)
        self.bin_idx_tree = [0]*(len(nums) + 1) # binary indexed tree
        for i, n in enumerate(nums): 
            self.update(i, n)

    def update(self, i: int, val: int) -> None:
        d, self.nums[i] = val - self.nums[i], val
        k = i + 1
        while k < len(self.bin_idx_tree):
            self.bin_idx_tree[k] += d
            k += (k & -k)

    def sumRange(self, i: int, j: int) -> int:
        return self.sumTo(j) - self.sumTo(i - 1)
    
    def sumTo(self, i: int) -> int:
        res = 0
        k = i + 1
        while k:
            res += self.bin_idx_tree[k]
            k -= (k & -k)
        return res