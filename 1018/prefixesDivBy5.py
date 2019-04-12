def prefixesDivBy5(self, A):
    tmp = A[:]
    for i in range(1, len(A)):
        tmp[i] += (tmp[i-1] << 1) % 5
    return [x % 5 == 0 for x in tmp]