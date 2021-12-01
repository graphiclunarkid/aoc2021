input = open('input', 'r')

depths = []
for line in input:
    depths.append(int(line[:len(line)-1]))

input.close()

count = 0

for i in range(1,len(depths)):
    if depths[i] > depths[i-1]:
        count += 1

print(count)
