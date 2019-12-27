inFile = open("in.txt", "r")
count = 0
for line in inFile:
    line = line.strip()
    print("Line %d (%d chars):" %(count, len(line)) + " " + line)
    count += 1
