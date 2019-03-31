def judgeCircle(self, moves: str) -> bool:
    count = {
        'R': 0, 'L': 0,
        'U': 0, 'D': 0
    }
        
    for m in moves: count[m] += 1
    return count['R'] == count['L'] and count['U'] == count['D']