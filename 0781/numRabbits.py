def numRabbits(self, answers: List[int]) -> int:
    res = 0
    count = collections.Counter(answers)
    for c in count:
    	# condition of count[c] > c+1 means that there are multiple color existed,
    	# each of colors has c+1 rabbits
        res += (count[c] + c)//(c + 1)*(c + 1) # plus c to fit the last color
    return res