def get_cages():
 cages = int(input("Number of cages: "))
 cages_count = 0
 tot_cages = []
 line_cage = []
 for cages_count in range (cages):
  cage_in = input("Cage number %d: " % cages_count)
  cage_in_list = cage_in.split()
  for arg in cage_in_list:
   arg = int(arg)
   line_cage.append(arg)
  tot_cages.append(line_cage)
  line_cage = []
 return tot_cages
def check_rows_valid(puzzle):
 for row in range(len(puzzle)):
    list1 = []
    for col in range(len(puzzle)):
      arg = puzzle[row][col]
      list1.append(arg)
      for num in list1:
     ))   if (list1.count(num) > 1 and num != 0):
           return False
 return True
def check_columns_valid(puzzle):
 for row in range(len(puzzle)):
  list1 = []
  for col in range(len(puzzle)):
    arg = puzzle[col][row]
    list1.append(arg)
    for num in list1:
     if (list1.count(num) > 1 and num != 0):
        return False
 return True
def check_one_cage_valid(list1,puzzle):  
  tot = list1[0]
  position = []
  sum = 0
  for pos in range(2, len(list1)):
    row = list1[pos]//5
    col = list1[pos]%5
    position.append(puzzle[row][col])
  for int in position:
     sum = sum + int
  if (position.count(0) >= 1):
      if (sum < tot):
        return True
      else:
        return False
  elif (sum != tot):
     return False
  return True
def check_cages_valid(puzzle, cages):
   bool_val = True
   list1 = 0
   while list1 < len(cages):
    if check_one_cage_valid(cages[list1],puzzle) == False:
     bool_val = False
     return False
    list1+=1
   return bool_val
 
def check_valid(puzzle, cages):
 if (check_cages_valid(puzzle, cages) == True and check_columns_valid(puzzle) == True and check_rows_valid(puzzle) == True):
  return True
 return False
 
