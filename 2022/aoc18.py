from collections import deque

# FILENAME = "aoc18-0.txt"
FILENAME = "aoc18-1.txt"

DIM = 3

def add(*args):
    return tuple(sum(vv) for vv in zip(*args))

def parse_droplets():
    with open(FILENAME, "r", encoding="utf-8") as file:
        return [tuple(int(v) for v in line.strip().split(',')) for line in file.readlines()]

def fill_space(pts, spc):
    for (x, y, z) in pts:
        spc[x][y][z] = True

def spatial_directions():
    for d in range(DIM):
        for s in (+1, -1):
            yield tuple(s if k == d else 0 for k in range(DIM))

SPATIAL_DIRECTIONS = tuple(spatial_directions())

# None: air / False: water / True: lava
def calc_surface(spc):
    o = 0
    for direction in SPATIAL_DIRECTIONS:
        for x in inner_range:
            for y in inner_range:
                for z in inner_range:
                    if not spc[x][y][z]:
                        continue
                    (u, v, w) = add((x, y, z), direction)
                    if spc[u][v][w] is None:
                        o += 1
    return o

def mark_outside(spc, x, y, z):
    queue = deque()
    queue.append((x, y, z))
    while queue:
        (x, y, z) = queue.popleft()
        if spc[x][y][z] is None:
            spc[x][y][z] = False
            for direction in SPATIAL_DIRECTIONS:
                (u, v, w) = add((x, y, z), direction)
                if (-1 <= u <= hi + 1) and (-1 <= v <= hi + 1) and (-1 <= w <= hi + 1):
                    queue.append((u, v, w))

points = parse_droplets()
# print(points)

lo = min(v for p in points for v in p)
hi = max(v for p in points for v in p)
inner_range = range(0, hi + 1)
outer_range = range(0, hi + 3)
# print(lo, hi)

space = [[[None for _ in outer_range] for _ in outer_range] for _ in outer_range]
fill_space(points, space)
# print(space)

surface = calc_surface(space)
print(surface)

mark_outside(space, hi + 1, hi + 1, hi + 1)
interior = calc_surface(space)
print(surface - interior)
