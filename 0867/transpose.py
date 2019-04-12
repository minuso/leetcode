def transpose(self, A):
    return [[r[i] for r in A] for i in range(len(A[0]))] # list comprehension
    #return list(zip(*A)) # zip method