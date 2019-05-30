class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = nums
        for i in range(1, len(self.sums)): # compute the sum of index 0 to index i
            self.sums[i] += self.sums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]