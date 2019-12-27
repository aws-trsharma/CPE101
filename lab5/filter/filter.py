from math import *
def are_positive(list1):
 positive = []
 count = 0
 while count < len(list1):
  if (list1[count] > 0):
   positive.append(list1[count])
   count+=1
  else:
   count+=1
 return positive
def are_greater_than_n (n, list1):
 greater = []
 count = 0
 for count in range(len(list1)):
  if (list1[count] > n):
   greater.append(list1[count])
   count += 1
  else:
    count+= 1
 return greater
def are_divisible_by_n (n, list1):
 divisible = [x for x in list1 if x%n==0]
 return divisible
