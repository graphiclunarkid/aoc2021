input = open('input', 'r')

depths = []
for line in input:
    depths.append(int(line[:len(line) - 1]))

input.close()

data = []
data = [depths[x] + depths[x + 1] + depths[x + 2] for x in range(0, len(depths) - 2)]

count = 0

for i in range(1, len(data)):
        
    if data[i] > data[i-1]:
        count += 1

print(count)
