from collections import Counter

def expand(points):
    start, end = points
    startx, starty = start
    endx, endy = end

    startx = int(startx)
    starty = int(starty)
    endx = int(endx)
    endy = int(endy)

    line = []
    if startx == endx:
        if starty < endy:
            line = [(startx, y) for y in range(starty, endy + 1)]
        else:
            line = [(startx, y) for y in range(endy, starty + 1)]
    elif starty == endy:
        if startx < endx:
            line = [(x, starty) for x in range(startx, endx + 1)]
        else:
            line = [(x, starty) for x in range(endx, startx + 1)]
    else:
        if startx < endx:
            line = list(zip(range(startx, endx + 1), range(starty, endy + 1)))
        else:
            line = list(zip(range(startx, endx - 1, -1), range(starty, endy + 1)))
    return(line)

def countHotSpots(ventMap):
    hotSpots = Counter(ventMap)
    hotSpots = {key:val for key, val in hotSpots.items() if val > 1}
    return(len(hotSpots))


with open('inputs/day5-input', 'r') as input:
    inputLines = []
    for line in input:
        inputLines.append(line.split())
        del inputLines[-1][1]

allLines = []
for line in inputLines:
    allLines.append([tuple(i.split(',')) for i in line])

ventMapPart1 = []
for line in allLines:
    if (line[0][1] == line[1][1]) or (line[0][0] == line[1][0]):
        ventMapPart1.extend(expand(line))

ventMapPart2 = []
for line in allLines:
    ventMapPart2.extend(expand(line))

print(f"Hotspots in part 1: {countHotSpots(ventMapPart1)}")
print(f"Hotspots in part 2: {countHotSpots(ventMapPart2)}")
