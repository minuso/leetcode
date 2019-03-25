def hammingDistance(self, x: int, y: int) -> int:
    x = x ^ y # do xor (and then count '1's)
    y = 0
    while x:
        y += 1
        x &= (x - 1) # useful tip for removing the last '1' bit
    return y