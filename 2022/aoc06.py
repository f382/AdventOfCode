#FILENAME = "aoc06-0.txt"
FILENAME = "aoc06-1.txt"

with open(FILENAME, "r", encoding="utf-8") as file:
    data = file.read()

#NEEDED = 4
NEEDED = 14

def isuniq(xx):
    return len(set(xx)) == len(xx)

def findmark(xx):
    for i, _ in enumerate(xx):
        j = i + NEEDED
        if isuniq(xx[i:j]):
            return j
    return None

m = findmark(data)

print(f"{m}")
