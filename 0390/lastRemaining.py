def lastRemaining(self, n: int) -> int:
   	head, d, left = 1, 1, 1        
   	while n > 1:
       	if left or n % 2: # current head will be removed
           	head += d
       	d, left = d << 1, left^1
       	n >>= 1
   	return head