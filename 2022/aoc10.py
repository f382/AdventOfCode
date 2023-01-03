# FILENAME = "aoc10-0.txt"
FILENAME = "aoc10-1.txt"

START_X = 1
CHECKPOINTS = (20, 60, 100, 140, 180, 220)
CRT_WIDTH = 40

def addx(x: int, value: int) -> int:
    return x + value

def noop(x: int) -> int:
    return x

INSTRUCTIONS = {'addx': (2, addx), 'noop': (1, noop)}

def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return [(instr, *(int(p) for p in params))
                for (instr, *params) in [line.strip().split() for line in file.readlines()]]

def execute(program: list, x: int):
    for (instr, *params) in program:
        (duration, function) = INSTRUCTIONS[instr]
        for _ in range(duration):
            yield x
        x = function(x, *params)

def main():
    program = parse_input(FILENAME)
    print(program)
    cycle = 1
    total = 0
    pixels = []
    for x in execute(program, START_X):
        if cycle in CHECKPOINTS:
            signal = cycle * x
            total += signal
            print(cycle, x, signal, total)
        (vert, horiz) = divmod(cycle - 1, CRT_WIDTH)
        lit = horiz - 1 <= x <= horiz + 1
        if vert >= len(pixels):
            pixels.append([])
        pixels[vert].append(lit)
        cycle += 1
    for row in pixels:
        print(''.join('#' if lit else '.' for lit in row))

if __name__ == '__main__':
    main()
