class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.poss = {}
        
    def insert(self, val):
        if val in self.poss: return False
        
        self.nums.append(val)
        self.poss[val] = len(self.nums) - 1
        return True
        
    def remove(self, val):
        if val not in self.poss: return False
        
        idx, last = self.poss[val], self.nums[-1]
        self.nums[idx], self.poss[last] = last, idx
        del self.nums[-1]
        del self.poss[val]
        return True
        
    def getRandom(self):
        return random.choice(self.nums)