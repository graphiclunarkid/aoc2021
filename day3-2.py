import numpy


def most_common(l):
    return(int((sum(l) >= len(l)/2)))

def pinpoint(haystack, sense=True, i=0):

    if len(haystack) == 1:
        [a] = haystack
        return(a)

    haystackT = numpy.transpose(haystack)
    if sense:
        val = most_common(haystackT[i])
    else:
        val = 1 - most_common(haystackT[i])

    return(pinpoint([needle for needle in haystack if needle[i] == val], sense, i+1))

def collapse_list(l):
    return(''.join(str(i) for i in l))


with open('inputs/day3-input', 'r') as input:
    diagnostics = []
    for line in input:
        diagnostics.append([int(i) for i in line[:len(line)-1]])

diagnosticsT = numpy.transpose(diagnostics)
gList = []
for line in diagnosticsT:
    gList.append(most_common(line))
eList = [int(not bit) for bit in gList]
gamma = collapse_list(gList)
epsilon = collapse_list(eList)

ogr = collapse_list(pinpoint(diagnostics, True))
csr = collapse_list(pinpoint(diagnostics, False))

print()
print(f"              Gamma: {gamma} ({int(gamma,2)})")
print(f"            Epsilon: {epsilon} ({int(epsilon,2)})")
print(f"  Power consumption: {int(gamma,2) * int(epsilon,2)}")
print()
print(f"O2 generator rating: {ogr} ({int(ogr,2)})")
print(f"CO2 scrubber rating: {csr} ({int(csr,2)})")
print(f"Life support rating: {int(ogr,2) * int(csr,2)}")
print()
