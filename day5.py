from collections import Counter

with open('inputs/day5-input', 'r') as input:
    inputLines = []
    for line in input:
        inputLines.append(line.split())
        del inputLines[-1][1]

allLines = []
for line in inputLines:
    allLines.append([i.split(',') for i in line])

horizLines, vertLines, diagLines = []
for line in allLines:
    if line[0][1] == line[1][1]:
        """ Horizontal """
        horizLines.append(line)
    elif line[0][0] == line[1][0]:
        """ Vertical """
        vertLines.append(line)
    else:
        """ Diagonal """
        diagLines.append(line)
