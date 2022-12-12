from heapq import *

# FILENAME = "aoc12-0.txt"
FILENAME = "aoc12-1.txt"

with open(FILENAME, "r", encoding="utf-8") as file:
    lines = [l.strip() for l in file.readlines()]

grid = [['a' if a == 'S' else 'z' if a == 'E' else a for a in line] for line in lines]
start = next((i, j) for (i, row) in enumerate(lines) for (j, a) in enumerate(row) if a == 'S')
goal = next((i, j) for (i, row) in enumerate(lines) for (j, a) in enumerate(row) if a == 'E')

d = {}
queue = [(0, goal)]

while queue:
    # print(len(queue))
    (c, (x, y)) = heappop(queue)
    if (x, y) in d:
        continue
    d[(x, y)] = c
    a = grid[x][y]
    if a == 'a':
        print((x, y), c)
        break
    for (i, j) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        p = x + i
        q = y + j
        if p < 0 or q < 0 or p >= len(grid) or q >= len(grid[p]):
            continue
        b = grid[p][q]
        if ord(b) < ord(a) - 1:
            continue
        if (p, q) in d:
            continue
        heappush(queue, (c + 1, (p, q)))
