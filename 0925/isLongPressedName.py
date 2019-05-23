def isLongPressedName(self, name: str, typed: str) -> bool:
    i, j = 0, 0
    while i < len(name) and j < len(typed):
        if name[i] == typed[j]: 
            i, j = i+1, j+1
        else:
            j += 1
    return i == len(name)