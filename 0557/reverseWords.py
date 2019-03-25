def reverseWords(self, s: str) -> str:
	# reverse the order of words and then reverse each word 
    return " ".join(s.split(" ")[::-1])[::-1]