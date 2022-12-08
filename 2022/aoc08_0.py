# FILENAME = "aoc08-0.txt"
FILENAME = "aoc08-1.txt"

with open(FILENAME, "r", encoding="utf-8") as file:
    lines = [l.strip() for l in file.readlines()]

def is_visible(x: int, y: int, p: int, q: int) -> bool:
    v = lines[x][y]
    x += p
    y += q
    while x >= 0 and y >= 0 and x < len(lines) and y < len(lines[x]):
        w = lines[x][y]
        if w >= v:
            return False
        x += p
        y += q
    return True

def is_vis(x: int, y: int) -> bool:
    return is_visible(x, y, -1, 0) or is_visible(x, y, 0, -1) or is_visible(x, y, +1, 0) or is_visible(x, y, 0, +1)

visible = [(x, y) for x in range(len(lines)) for y in range(len(lines[x])) if is_vis(x, y)]

c = len(visible)
print(c)
