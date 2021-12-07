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
            line = [(startx, y) for y in range(starty,endy + 1)]
        else:
            line = [(startx, y) for y in range(endy,starty + 1)]
    elif starty == endy:
        if startx < endx:
            line = [(x, starty) for x in range(startx,endx + 1)]
        else:
            line = [(x, starty) for x in range(endx,startx + 1)]
    else:
        raise ValueError

    return(line)


with open('inputs/day5-input', 'r') as input:
    inputLines = []
    for line in input:
        inputLines.append(line.split())
        del inputLines[-1][1]

allLines = []
for line in inputLines:
    allLines.append([tuple(i.split(',')) for i in line])

horizLines = []
vertLines = []
diagLines = []
ventMap = []
for line in allLines:
    if line[0][1] == line[1][1]:
        """ Horizontal """
        horizLines.append(line)
        ventMap.extend(expand(line))
    elif line[0][0] == line[1][0]:
        """ Vertical """
        vertLines.append(line)
        ventMap.extend(expand(line))
    else:
        """ Diagonal """
        diagLines.append(line)

hotSpots = Counter(ventMap)
hotSpots = {key:val for key, val in hotSpots.items() if val > 1}
print(f"{len(hotSpots)}")
