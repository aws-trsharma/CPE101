import driver

def letter (row, col):
 if (row == col) or (6 - col == row):
  return 'X'
 else:
  return 'O'
if __name__ == '__main__':
    driver.comparePatterns(letter)


