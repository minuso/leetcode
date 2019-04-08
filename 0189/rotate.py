def rotate(self, nums: List[int], k: int) -> None:
    nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]