def canJump(self, nums: List[int]) -> bool:
    nums[-1] = 1 # last jump (target position) can not be 0
    zero_pos2len = {} # length of continous zeros (except the target position)
    for p, jump in enumerate(nums):
        if jump == 0:
            pos = p
            while nums[p] == 0: p += 1 # never out of range bacause the last jump is not 0
            zero_pos2len[pos] = p - pos
                
    for pos in zero_pos2len:
        j = pos
        while j >= 0:
            if nums[j] > zero_pos2len[pos] + (pos - j) - 1:
                break 
            j -= 1
        if j == -1: # there is no previous jump can jump over the current zeros
            return False
    return True