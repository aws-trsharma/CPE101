class Point:
    """ A class to represent a point in the x-y plane
    Attributes:
        x - x-coordinate an int
        y - y-coordinate an int"""
    def __init__(self, x, y):
      self.x = x
      self.y = y
class Circle:
     """A class to represent a circle with it's center point and radius
     Attributes:
        center - center (object from point method) an int
        radius - radius of the circle:  an int"""
     def __init__(self, center, radius):
         self.center = center
         self.radius = radius
