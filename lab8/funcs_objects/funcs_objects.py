from objects import *
from math import *
def distance(pt1, pt2):
   return sqrt((pt2.x-pt1.x)**2+(pt2.y-pt1.y)**2)
def circles_overlap(c1, c2):
   center_dist = sqrt((c1.center.x-c2.center.x)**2+(c1.center.y-c2.center.y)**2)
   rad_dist = (c1.radius + c2.radius)
   return center_dist <= rad_dist
