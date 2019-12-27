from objects import *
from math import *
def distance_all(list1):     
   return [sqrt((pt.y)**2+(pt.x)**2) for pt in list1]
def are_in_first_quadrant(list1):
    return [pt for pt in list1 if pt.x  > 0 and pt.y >0]
