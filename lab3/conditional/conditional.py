def max_101(x,y):
 max = 0
 if ( x > y):
  max = x
 elif ( x < y):
  max = y
 else: 
  max = x
 return max
def max_of_three(x,y,z):
 max = 0
 if (x >= y) and (x >= z):
  max = x
 elif ( y >= x ) and (y >= z):
  max = y
 elif (z >= y) and (z >= x):
  max = z
 return max
def rental_late_fee(days):
 fee = 0
 if (days <= 0):
  fee = 0
 elif(days <= 9):
  fee = 5
 elif(days <= 15):
  fee = 7
 elif (days <= 24):
  fee = 19
 else:
  fee = 100 
 return fee
