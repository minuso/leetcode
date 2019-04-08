def maximalSquare(self, matrix: List[List[str]]) -> int:
    if len([1 for r in matrix if '1' in r]) == 0: return 0 # no '1' in matrix
        
    max_wid = 1 # width of max square
    pre_row = [int(b) for b in matrix[0]]
    for r in matrix[1:]:
        cur_row = [int(b) for b in r]
        for i in range(1, len(cur_row)):
            if cur_row[i] == 1:
                cur_row[i] = min(cur_row[i-1], pre_row[i], pre_row[i-1]) + 1 # dynamic programming
                max_wid = max(max_wid, cur_row[i])
        pre_row = cur_row
    return max_wid**2