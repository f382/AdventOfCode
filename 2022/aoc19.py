from dataclasses import dataclass
import re
import sys


# FILENAME = "aoc19-0.txt"
FILENAME = "aoc19-1.txt"

TIME = 24
# TIME = 32
INFINITY = sys.maxsize
START_ROBOTS = (1, 0, 0, 0)
START_RESOURCES = (0, 0, 0, 0)

N = len(START_ROBOTS)
ZERO_QUAD = tuple(0 for _ in range(N))
SINGLETON_QUADS = tuple(tuple(int(j == k) for j in range(N)) for k in range(N))


@dataclass
class Blueprint:
    idnum: int
    costs: tuple
    maxgeo: int = 0

    def quality_level(self) -> int:
        return self.idnum * self.maxgeo


def parse_input(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file.readlines():
            if m := re.match(r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.',
                             line.strip()):
                yield Blueprint(idnum = int(m.group(1)),
                                costs = ((int(m.group(2)), 0, 0, 0),
                                         (int(m.group(3)), 0, 0, 0),
                                         (int(m.group(4)), int(m.group(5)), 0, 0),
                                         (int(m.group(6)), 0, int(m.group(7)), 0)))

def add(*args: int) -> tuple:
    return tuple(sum(t) for t in zip(*args))

def multiply(cost, count: int) -> tuple:
    return tuple(price * count for price in cost)

def subtract(resources, cost) -> tuple:
    return tuple(amount - price for (amount, price) in zip(resources, cost))

def divide(resources, cost) -> int:
    return int(greater_or_equal(resources, cost))

def greater_or_equal(resources, cost) -> bool:
    return all(amount >= price for (amount, price) in zip(resources, cost))

def multisubtract(resources, costs, counts) -> tuple:
    rest = resources
    for (c, n) in zip(costs, counts):
        rest = subtract(rest, multiply(c, n))
    return rest

def max_possibility(costs, resources) -> tuple:
    return tuple(divide(resources, c) for c in costs)

def find_done_robots(costs: tuple, robots: tuple, time: int, done_robots: int) -> int:
    k = N - 1
    while (k := k - 1) >= done_robots:
        if time <= N - k or all(robots[k] >= costs[j][k] for j in range(k + 1, N) if time > N - j):
            return k + 1
    return done_robots

def calc_top(possibilities) -> tuple:
    return tuple(max(t) for t in zip(*possibilities))

def calc_bottom(possibilities) -> tuple:
    return tuple(min(t) for t in zip(*possibilities))

def find_possibilities(costs: tuple, robots: tuple, resources: tuple, done_robots: int):
    has_all = True
    has_any = False
    k = N
    while (k := k - 1) >= done_robots:
        if greater_or_equal(resources, costs[k]):
            has_any = True
            yield SINGLETON_QUADS[k]
        elif (k == 0 or robots[k - 1] > 0) and done_robots == 0:
            has_all = False
    if has_any and has_all:
        return
    yield ZERO_QUAD

def upper_bound(blueprint: Blueprint, robots: tuple, resources: tuple, time: int) -> int:
    geodes = resources[-1]
    if time == 0:
        return geodes
    if geodes > blueprint.maxgeo:
        return INFINITY
    p = max_possibility(blueprint.costs, resources)
    bound = upper_bound(blueprint,
                        add(robots, p),
                        add(resources, robots),
                        time - 1)
    return bound

def calculate(blueprint: Blueprint, robots: tuple, resources: tuple, time: int, done_robots: int) -> int:
    geodes = resources[-1]
    if geodes > blueprint.maxgeo:
        blueprint.maxgeo = geodes
    if time == 0:
        return geodes
    done_robots = find_done_robots(blueprint.costs, robots, time, done_robots)
    possibilities = list(find_possibilities(blueprint.costs, robots, resources, done_robots))
    if len(possibilities) > 1:
        (top, bottom) = (calc_top(possibilities), calc_bottom(possibilities))
        bound = upper_bound(blueprint,
                            add(robots, top),
                            add(multisubtract(resources, blueprint.costs, bottom), robots),
                            time - 1)
        if bound <= blueprint.maxgeo:
            return 0
    return max((calculate(blueprint,
                          add(robots, p),
                          add(multisubtract(resources, blueprint.costs, p), robots),
                          time - 1,
                          done_robots)
                for p in possibilities),
               default = 0)

def test():
    assert ZERO_QUAD == (0, 0, 0, 0)
    assert SINGLETON_QUADS == ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
    assert add((1, 2, 3), (2, -4, 5)) == (3, -2, 8)
    assert multiply((7, 0, 4), 3) == (21, 0, 12)
    assert subtract((5, 1, 2), (4, 1, 7)) == (1, 0, -5)
    assert divide((13, 2, 5), (3, 0, 2)) == 1
    assert divide((13, 0, 5), (23, 0, 2)) == 0
    assert greater_or_equal((7, 5, 4), (4, 5, 2)) and not greater_or_equal((3, 5, 4), (4, 5, 2))
    assert multisubtract((90, 43, 37), ((4, 5, 2), (13, 2, 5)), (1, 2)) == (60, 34, 25)
    assert max_possibility(((4, 5, 2), (13, 2, 5), (3, 0, 2), (4, 1, 7)), (90, 43, 37)) == (1, 1, 1, 1)
    assert list(find_possibilities(((8, 5, 2), (13, 2, 5), (3, 0, 30), (4, 50, 7)), (1, 1, 1), (30, 43, 37), 0)) == [
        (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0)]

def main():
    test()
    blueprints = list(parse_input(FILENAME))
    # for b in blueprints:
    #     print(b)
    qty_lvl_sum = 0
    max_geo_prd = 1
    for b in blueprints:
        calculate(b, START_ROBOTS, START_RESOURCES, TIME, 0)
        print(b, b.quality_level())
        qty_lvl_sum += b.quality_level()
        max_geo_prd *= b.maxgeo
        print(f'{qty_lvl_sum=}, {max_geo_prd=}')


if __name__ == '__main__':
    main()
