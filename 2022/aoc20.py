# FILENAME = "aoc20-0.txt"
FILENAME = "aoc20-1.txt"

KEY = 1
COUNT = 1
# KEY = 811589153
# COUNT = 10


def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return list(enumerate(int(line.strip()) * KEY for line in file.readlines()))

def calc_pos(data: list) -> dict:
    return {t: i for (i, t) in enumerate(data)}

def mix(data: list, pos: dict, t: tuple):
    (_, n) = t
    p = pos[t]
    assert data.pop(p) == t
    q = (p + n - 1) % len(data) + 1
    assert 1 <= q <= len(data)
    data.insert(q, t)
    (l, r) = (min(p, q), (max(p, q)))
    for j in range(l, r + 1):
        m = data[j]
        pos[m] = j
    # print(data, pos, t)

def mix_all(data: list, pos: dict):
    copied = data[:]
    for _ in range(COUNT):
        for t in copied:
            mix(data, pos, t)

def coord_sum(data):
    # print(data)
    p = next(j for (j, (_, m)) in enumerate(data) if m == 0)
    # print(p)
    return sum(data[(p + k) % len(data)][1] for k in (1000, 2000, 3000))

def main():
    data = parse_input(FILENAME)
    pos = calc_pos(data)
    print(data, pos)
    mix_all(data, pos)
    print(coord_sum(data))


if __name__ == '__main__':
    main()
