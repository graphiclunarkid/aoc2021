import numpy

# Read input from file
# Split each input line into a list to create a 2d array
# Convert to integers at the same time

with open('inputs/day3-input', 'r') as input:
    diagnostics = []
    for line in input:
        diagnostics.append([int(i) for i in line[:len(line)-1]])

# Transpose the array
diagnosticsT = numpy.transpose(diagnostics)

# Count the number of 1s in each line
# Set gamma bit to 1 if line is mostly 1s else 0
gList = []
for line in diagnosticsT:
    gList.append(int((sum(line) > len(line)/2)))

# Epsilon is the inverse of gamma
eList = []
eList = [int(not bit) for bit in gList]

# Collapse lists into strings
gamma = ''.join(str(g) for g in gList)
epsilon = ''.join(str(e) for e in eList)

print(f"Gamma: 0b{gamma} ({int(gamma,2)})")
print(f"Epsilon: 0b{epsilon} ({int(epsilon,2)})")

# Multiply Gamma by Epsilon
# Print result
print(f"Power consumption: {int(gamma,2) * int(epsilon,2)} W")
