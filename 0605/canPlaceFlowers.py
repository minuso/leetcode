def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
	# [-2] and [len(flowerbed) + 1] are used to avoid head-0 and tail-0 conditions
    f = [-2] + [i for i, x in enumerate(flowerbed) if x] + [len(flowerbed) + 1]
    max_n = sum(abs(f[i]-f[i-1]-2)//2 for i in range(1, len(f)))
    return max_n >= n