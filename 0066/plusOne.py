def plusOne(self, digits):
    for i in range(len(digits)):
        if digits[~i] == 9:
            digits[~i] = 0
        else:
            digits[~i] += 1
            return digits
    return [1] + digits