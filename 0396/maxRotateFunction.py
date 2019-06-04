def maxRotateFunction(self, A: List[int]) -> int:
    res = tmp = sum([i*v for i, v in enumerate(A)])
    arr_sum = sum(A)
    for i in range(1, len(A)):
        # sum of rotation in the current round
        # is 'add' every elements (except the last (A[-i]))
        # and 'subtract' the last term (A[-i]*(n-1))
        # => add the sum (including the last) and subtract the last n times
        tmp += (arr_sum - A[-i]*len(A))
        res = max(res, tmp)
    return res