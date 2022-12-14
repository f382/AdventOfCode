# FILENAME = "aoc14-0.txt"
FILENAME = "aoc14-1.txt"

with open(FILENAME, "r", encoding="utf-8") as file:
    lines = [l.strip() for l in file.readlines()]

paths = [[[int(v) for v in p.split(',')] for p in l] for l in [l.split(' -> ') for l in lines]]
# print(paths)

hi = max(v for l in paths for p in l for v in p)
hi_y = max(p[1] for l in paths for p in l)

grid = [['.' for _ in range(2 * hi + 2)] for _ in range(2 * hi + 2)]

def sign(v):
    return 1 if v > 0 else -1 if v < 0 else 0

for l in paths:
    pos = l[0]
    for p in l[1:]:
        s = (sign(p[0] - pos[0]), sign(p[1] - pos[1]))
        while True:
            grid[pos[0]][pos[1]] = '#'
            if pos == p:
                break
            pos[0] += s[0]
            pos[1] += s[1]
# print(grid)

SAND = [500, 0]
grid[SAND[0]][SAND[1]] = '+'

pos = None
c = 0

while True:
    if pos is None:
        pos = SAND[:]
    if pos[1] <= hi_y and grid[pos[0]][pos[1] + 1] in ('.', '~'):
        pos[1] += 1
    elif pos[1] <= hi_y and grid[pos[0] - 1][pos[1] + 1] in ('.', '~'):
        pos[0] -= 1
        pos[1] += 1
    elif pos[1] <= hi_y and grid[pos[0] + 1][pos[1] + 1] in ('.', '~'):
        pos[0] += 1
        pos[1] += 1
    else:
        grid[pos[0]][pos[1]] = 'o'
        c += 1
        if pos == SAND:
            break
        pos = None
        # for j in range(0, 12):
        #     print(''.join([grid[i][j] for i in range(hi - 17, hi + 12)]))
        # print()
        continue
    # if grid[pos[0]][pos[1]] == '.':
    #     grid[pos[0]][pos[1]] = '~'

print(c)
