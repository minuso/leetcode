def bulbSwitch(self, n: int) -> int:
	# find the count of number which has odd (2k+1) factors
	# factors are pairs (a,b) s.t. a*b = n
	# only square number has odd count of factors: has a factor pair (a,a)
    return int(math.sqrt(n))