def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    res = []
    for num in range(left, right+1):
        flag, tmp = True, num
        while tmp:
            if tmp % 10 == 0:
                flag = False
                break
            if num % (tmp%10):
                flag = False
                break
            tmp //= 10
                
        if flag:
            res.append(num)
    return res