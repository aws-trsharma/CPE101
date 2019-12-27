from sys import *

def readFile(inFile):
   int1 = 0
   float1 = 0
   other = 0
   sum1 = 0
   for line in inFile:
     line = line.split()
     for val in line:
      try: 
        val = int(val)
        int1 += 1
        sum1 += val
      except:
         try: 
           val = float(val)
           float1 += 1
           sum1 += val
         except:
           other += 1
   print("Ints:",  int1)
   print("  Floats:", float1)
   print("  Other:", other)
   return sum1
if len(argv) <= 3 and len(argv) >= 2:
   if len(argv) == 3:
    if argv[1] == "-s":
      inFile = open(argv[2], 'r')
      sum1 = readFile(inFile)
      print("Sum: %.2f" %sum1)
    elif argv[2] == "-s":
      inFile = open(argv[1], 'r')
      sum1 = readFile(inFile)
      print("Sum: %.2f" %sum1)
    else:
      print("Usage: [-s] file_name")
      exit()
   else:
      try:
         inFile = open(argv[1], 'r')
         readFile(inFile)
      except:
         print("Unable to open %s"  %argv[1])
else:
   print("Usage: [-s] file_name")
   exit()


