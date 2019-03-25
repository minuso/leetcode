def numberOfLines(self, widths: List[int], S: str) -> List[int]:
    if not S: return [0, 0] # exception of at-least-1-line assumption
    LINE_LIMIT, BASE = 100, ord('a')
        
    l_count, cur_width = 1, 0
    for c in S:
        wid = widths[ord(c) - BASE]
        cur_width += wid
        if cur_width > LINE_LIMIT:
            l_count += 1    # move to the new line
            cur_width = wid # write the current character
    return [l_count, cur_width]