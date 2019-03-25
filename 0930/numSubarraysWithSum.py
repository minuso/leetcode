def numSubarraysWithSum(self, A: List[int], S: int) -> int:
    if sum(A) < S or S < 0: return 0 # no combination case

    # special case: sum of (1+2+...+len) of each max-len-all-0 subarray
    if S == 0:
        str_with_01 = ''.join([str(n) for n in A])
        zero_lens = [len(zeros) for zeros in str_with_01.split('1')]
        return sum([(1 + len)*len//2 for len in zero_lens]) # formula of (1+2+...+len)

    ones = [-1] + [i for i in range(len(A)) if (A[i] == 1)] + [len(A)]

    res = 0
    l, r = 1, S # the interval of the first smallest subarray
    while (r+1) < len(ones):
        res += (ones[l] - ones[l-1])*(ones[r+1] - ones[r]) # equal to the codes below
        #num_f0, num_b0 = (ones[l] - ones[l-1] - 1), (ones[r+1] - ones[r] - 1)
        #res += (num_f0 + 1)*(num_b0 + 1)
        l, r = l+1, r+1
    return res