
def puzzle_to_lists(puzzle):
    val = 0
    full_cage = []
    for row in range(10):
        res = []
        for col in range(10):
            res.append(puzzle[col])
        puzzle = puzzle[10:]
        full_cage.append(res)
    return full_cage
def checkRows(puzzle, word):
   row_answer = []
   for row in range(len(puzzle)):
      list1 = []
      for col in range(len(puzzle)):
         arg = puzzle[row][col]
         list1.append(arg)
      list1 = ''.join(list1)
      if list1.find(word) != -1:
         row_answer.append(row)
         row_answer.append(list1.find(word))
         return row_answer 
   return False
def checkColumns(puzzle, word):
    col_answer = []
    for row in range(len(puzzle)):
        list1 = []
        for col in range(len(puzzle)):
            arg = puzzle[col][row]
            list1.append(arg)
        list1 = ''.join(list1)
        if list1.find(word) != -1:
           col_answer.append(row)
           col_answer.append(list1.find(word))
           col_answer[0], col_answer[1] = col_answer[1], col_answer[0]
           return col_answer
    return False
def checkColumnsBackwards(puzzle,word):
    col_backwards = []
    for row in range(len(puzzle)):
        list1 = []
        for col in range(len(puzzle)):
            arg = puzzle[col][row]
            list1.append(arg)
        list1 = list1[::-1]  #google
        list1 = ''.join(list1)
        if list1.find(word) != -1:
            col_backwards.append(row)
            col_backwards.append(9-list1.find(word))
            col_backwards[0], col_backwards[1] = col_backwards[1], col_backwards[0]
            return col_backwards
    return False
def checkRowBackwards(puzzle, word):
    row_back = []
    for row in range(len(puzzle)):
        list1 = list(puzzle[row])
        list1 = list1[::-1] #google
        list1 = ''.join(list1)
        if list1.find(word) != -1:
           row_back.append(row)
           row_back.append(9-list1.find(word))
           return row_back
    return False
def checkDiagonal(puzzle, word):
 diagonal = []
 for row in range(len(puzzle)):
   for col in range(len(puzzle)):
      list1 = []
      i = 0
      while (row + i < 10 and col + i < 10):
         arg = puzzle[row + i] [col + i]
         list1.append(arg)
         i+=1
      list1 = ''.join(list1)
      if list1.find(word)!= -1:
         i = list1.find(word)
         diagonal.append(row+i)
         diagonal.append(col+i)
         return diagonal 
 return False

