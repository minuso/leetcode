def countBits(self, num: int) -> List[int]:
	# head-1 extension
    res = [0, 1]
    while len(res) < num + 1:
        res.extend([c + 1 for c in res]) # add head-1 causes count plus 1
    return res[:num+1]

    # dynamic programming
    #res = [0]*(num+1)
    #for i in range(1, num + 1):
    #    res[i] = res[i >> 1] + (i&1) # res[i >> 1] must had been stored
    #return res