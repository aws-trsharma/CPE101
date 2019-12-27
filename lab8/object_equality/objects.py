from utility import *
class Point:

   """ A class to represent a point in the x-y plane
   Attributes:
     x - x-coordinate an int
     y - y-coordinate an int"""
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def __eq__(self, other):
      return epsilon_equal(self.x ,other.x) and epsilon_equal(self.y, other.y)
