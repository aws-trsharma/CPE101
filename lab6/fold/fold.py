
def sum(list1):
   sum = 0
   for num in range(len(list1)):
      sum += list1[num]
   return sum
def index_of_smallest(list1):
   if (len(list1) <= 0):
     return -1 
   else: 
     count = list1[0]
     small = 0
     for i in range(len(list1)):
       if (count > list1[i]):
          count = list1[i]
          small = i
     return small
