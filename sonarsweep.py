with open('day1-input', 'r') as input:
    readings = []
    for line in input:
        readings.append(int(line[:len(line)-1]))

def smooth(granular):
    return([granular[x] + granular[x+1] + granular[x+2] for x in range(0,len(granular)-2)])

def count(readings):
    return(len([i for i in range(1,len(readings)) if readings[i] > readings[i-1]]))

print(f"Count: {count(readings)}")
print(f"Noise-reduced count: {count(smooth(readings))}")
