def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    for n in nums:
        if n in count: count[n] += 1
        else: count[n] = 1
        
    res = [n for n in sorted(count, key=count.get, reverse=True)] # sort by value
    return res[:k]