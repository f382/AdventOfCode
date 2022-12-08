# FILENAME = "aoc08-0.txt"
FILENAME = "aoc08-1.txt"

with open(FILENAME, "r", encoding="utf-8") as file:
    lines = [l.strip() for l in file.readlines()]

def is_visible(x: int, y: int, p: int, q: int) -> int:
    v = lines[x][y]
    s = 0
    x += p
    y += q
    while x >= 0 and y >= 0 and x < len(lines) and y < len(lines[x]):
        w = lines[x][y]
        s += 1
        if w >= v:
            return s
        x += p
        y += q
    return s

def is_vis(x: int, y: int) -> int:
    return is_visible(x, y, -1, 0) * is_visible(x, y, 0, -1) * is_visible(x, y, +1, 0) * is_visible(x, y, 0, +1)

visible = [is_vis(x, y) for x in range(len(lines)) for y in range(len(lines[x]))]

c = max(visible)
print(c)
