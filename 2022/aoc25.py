# FILENAME='aoc25-0.txt'
FILENAME='aoc25-1.txt'


BASE = 5
BOUND = 3
NEG_DIGITS = ('=', '-')

def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def to_snafu(num: int, base: int = BASE, bound: int = BOUND) -> str:
    if num >= bound or num < bound - base:
        (q, r) = divmod(num, base)
        if r >= bound:
            q += 1
            r -= base
        prefix = to_snafu(q, base, bound)
    else:
        r = num
        prefix = ''
    txt = str(r) if r >= 0 else NEG_DIGITS[r]
    return prefix + txt

def from_snafu(txt: str, base: int = BASE, bound: int = BOUND) -> int:
    if not txt:
        return 0
    r = txt[-1]
    r = int(r) if r.isdigit() else NEG_DIGITS.index(r) - len(NEG_DIGITS)
    return from_snafu(txt[:-1], base, bound) * base + r

def test():
    assert to_snafu(0) == '0'
    assert to_snafu(4) == '1-'
    assert to_snafu(-2) == '='
    assert to_snafu(-3) == '-2'
    assert from_snafu('0') == 0
    assert from_snafu('1=') == 3
    assert from_snafu('-') == -1
    assert from_snafu('=2') == -8

def main():
    test()
    lines = parse_input(FILENAME)
    total = sum(from_snafu(line) for line in lines)
    snafu = to_snafu(total)
    print(total, snafu)


if __name__ == '__main__':
    main()
