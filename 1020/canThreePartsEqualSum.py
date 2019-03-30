def canThreePartsEqualSum(self, A: List[int]) -> bool:
    part_sum = sum(A)/3
    if part_sum != int(part_sum): return False # can not divided by 3
        
    cur_sum = 0
    for n in A:
        cur_sum += n
        cur_sum = 0 if cur_sum == part_sum else cur_sum
    return cur_sum == 0