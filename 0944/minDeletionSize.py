def minDeletionSize(self, A: List[str]) -> int:
	# list comprehension with zip(*A) (the transpose of A)
	return sum([1 for s in zip(*A) if sorted(s) != list(s)])