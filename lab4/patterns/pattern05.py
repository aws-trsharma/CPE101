import driver

def letter(row, col):
  if ( row > 0 and col < row):
     return 'T'
  else:
     return 'W'

if __name__ == '__main__':
    driver.comparePatterns(letter)


