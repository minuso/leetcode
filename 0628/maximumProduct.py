def maximumProduct(self, nums: List[int]) -> int:
    max_1, max_2, max_3 = float('-inf'), float('-inf'), float('-inf')
    min_1, min_2 = float('inf'), float('inf') # product of two negative number is positive
    for n in nums:
        if n > max_1:
            max_1, max_2, max_3 = n, max_1, max_2
        elif n > max_2:
            max_2, max_3 = n, max_2
        elif n > max_3:
            max_3 = n
                
        if n < min_1: # must use new if statement
            min_1, min_2 = n, min_1
        elif n < min_2:
            min_2 = n
    return max(max_1*max_2*max_3, max_1*min_1*min_2)