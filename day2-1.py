with open('inputs/day2-input', 'r') as input:
    commands = []
    for line in input:
        commands.append(line[:len(line)-1])

directions = [command.split(' ') for command in commands]

horiz = sum([int(value) for direction,value in directions if direction == "forward"])
down  = sum([int(value) for direction,value in directions if direction == "down"])
up    = sum([int(value) for direction,value in directions if direction == "up"])
depth = down - up

print(f"Horizontal position: {horiz}")
print(f"Depth: {depth}")
print(f"Product: {horiz * depth}")
