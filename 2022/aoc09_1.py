# FILENAME = "aoc09-0.txt"
FILENAME = "aoc09-1.txt"

TRANS = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

with open(FILENAME, "r", encoding="utf-8") as file:
    lines = [l.strip() for l in file.readlines()]

def sign(x: int, low: int = 0) -> int:
    return 1 if x > low else -1 if x < -low else 0

moves = [(TRANS[d], int(c)) for (d, c) in (l.split() for l in lines)]
# print(moves)
s = set()
c = 0
tt = [(0, 0)] * 10
mm = [(0, 0)] * 10
while moves or c or any(m[0] for m in mm) or any(m[1] for m in mm):
    print(f'{c=}, {tt=}, {mm=}')
    s.add(tt[-1])
    if not c:
        if moves:
            (d, c) = moves.pop(0)
        else:
            d = (0, 0)
        mm[0] = d
    for (i, t) in enumerate(tt):
        m = mm[i]
        if i > 0:
            h = tt[i - 1]
            m = (sign(h[0] - t[0], 1), sign(h[1] - t[1], 1))
            if m != (0, 0):
                m = (sign(h[0] - t[0], 0), sign(h[1] - t[1], 0))
        t = (t[0] + m[0], t[1] + m[1])
        tt[i] = t
        mm[i] = m
    if c > 0:
        c -= 1
s.add(tt[-1])

print(len(s))
