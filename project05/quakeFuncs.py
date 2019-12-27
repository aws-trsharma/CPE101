from urllib.request import *
from json import *
from datetime import *
from operator import *

# GIVEN FUNCTIONS:
# Use these two as-is and do not change them
def get_json(url):
   ''' Function to get a json dictionary from a website.
       url - a string'''
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   ''' Converts integer seconds since epoch to a string.
       time - an int '''
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    
def epsilon_equal(n,m,epsilon = 0.00001):
    return (n-epsilon < m) and (n+epsilon > m)
# Add Earthquake class definition here   
class Earthquake:
     """A class to represent a Earthquake in a specific format
     Attributes:
          place - location a string
          mag - magnitude a int
          latitude - latitude a int
          time - time a int
          longitude - longitude a int"""
     def __init__(self, place,mag, longitude, latitude, time):
         self.mag = mag
         self.place = place
         self.time = time
         self.longitude = longitude
         self.latitude = latitude
     def __eq__(self, other):
         return (epsilon_equal(self.mag, other.mag) and epsilon_equal(self.time, other.time) and 
         self.place== other.place and epsilon_equal(self.longitude,other.longitude) 
         and epsilon_equal(self.latitude, other.latitude))
     def __str__(self):
         return ("(%.2f)%41s at %s (%8.3f, %.3f)" %(self.mag, self.place, 
         time_to_str(self.time), self.longitude, self.latitude))
     def __repr__(self):
        return (str(self.mag) + " " +  str(self.longitude) + " " + str(self.latitude) + " " + str(self.time) + " " +  str(self.place))
# Required function - implement mei!   
def read_quakes_from_file(filename):
   inFile = open(filename, "r")
   list1 = []
   for line in inFile:
       line = line.split()
       mag = float(line[0])
       longitude = float(line[1])
       latitude = float(line[2])
       time = int(line[3])
       string = " ".join(line[4:])
       place = string
       quake = Earthquake(place,mag,longitude,latitude,time)
       list1.append(quake)
   inFile.close()
   return list1
# Required function - implement me!
def filter_by_mag(quakes, low, high):
   list1 = []
   for quake in quakes:
      mag = quake.mag
      if mag >= low and mag <= high:
         list1.append(quake)
   return list1
     
# Required function - implement me!
def filter_by_place(quakes, word):   
   list1 = []
   upper = word.upper()
   word = word.lower()
   for quake in quakes: 
       place = quake.place
       place = place.lower()
       if place.find(word)!=-1:
          list1.append(quake)
   return list1

# Required function for final part - implement me too!   
def quake_from_feature(feature):
         place = feature["properties"]["place"]
         mag = feature["properties"]["mag"]
         time = feature["properties"]["time"]
         time = int(time * 0.001)
         longitude = feature["geometry"]["coordinates"][0]
         latitude = feature["geometry"]["coordinates"][1]
         quake = Earthquake(place, mag, longitude, latitude, time)
         return quake


   
