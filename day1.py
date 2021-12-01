input = open('input', 'r')

depths = []
for line in input:
    depths.append(line[:len(line)-1])

input.close()

print(depths)

