def arrangeCoins(self, n: int) -> int:
	# solve (1+x)*x/2 = n in 'int'
	# equation is x^2 + x - 2n = 0 => (a, b, c) = (1, 1, -2n) 
	# formula is (-b +- sqrt(b^2 - 4ac)) / 2a
	# positive solution: (-b + sqrt(b^2 - 4ac)) / 2a
    return int((-1 + math.sqrt(1 + 8*n))/2.0)