def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    for row in A:
        l, r = 0, len(row) - 1
        while l <= r:
            if row[l] == row[r]:    		 # row[l] != row[r]: results in the same as origin
                row[l] = row[r] = 1 ^ row[l] # row[l] == row[r]: only needs to invert
            l, r = l+1, r-1
    return A