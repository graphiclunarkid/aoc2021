with open('inputs/day2-input', 'r') as input:
    commands = []
    for line in input:
        commands.append(line[:len(line)-1])

directions = [command.split(' ') for command in commands]
aim = 0
horiz = 0
depth = 0

for direction in directions:
    if direction[0] == "forward":
        horiz += int(direction[1])
        depth += int(direction[1]) * aim
    elif direction[0] == "down":
        aim += int(direction[1])
    elif direction[0] == "up":
        aim -= int(direction[1])

print(f"Aim: {aim}")
print(f"Horizontal position: {horiz}")
print(f"Depth: {depth}")
print(f"Product: {horiz * depth}")
