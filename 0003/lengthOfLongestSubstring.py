def lengthOfLongestSubstring(self, s: str) -> int:
	cur_sub, max_len = '', 0
    for c in s:
 		if c in cur_sub: # need update cur_sub
			max_len = max(len(cur_sub), max_len) # update max_len first
        	cur_sub = cur_sub[cur_sub.index(c) + 1:] # cut the repeating c
        cur_sub += c
    return max(len(cur_sub), max_len) # exception: s is the longest one