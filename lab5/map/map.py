
from math import *
def square_all(list1):
 squared = []
 for n in list1:
  squared.append(n**2)
 return squared
def add_n_all(n,list1):
 squared = []
 count = 0
 while count < len(list1):
  squared.append(n+list1[count])
  count += 1
 return squared
def even_or_odd_all(list1):
 boolean = [True if n%2==0 else False  for n in list1]
 return boolean
