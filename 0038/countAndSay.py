def countAndSay(self, n):
    cur, res = 1, '1'
    while cur < n:
        tmp = ''
        count, say = 1, res[0]
        for i in range(1, len(res)):
            if res[i] == say:
                count += 1
            else:
                tmp += str(count) + say
                count, say = 1, res[i]
        tmp += str(count) + say # the last count-say
        cur, res = cur+1, tmp
    return res