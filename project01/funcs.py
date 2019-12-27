from math import *
def poundsToKG(pounds):
      #takes pounds and converts it into kg
      kg  = pounds * 0.453592
      return kg
def getMassObject(object):
      #takes character of object which is being thrown and returns 
      #mass of object
      kg = 0.0
      if (object == 't'): #obj is tomato
         kg = 0.1
      elif (object =='p'): #obj is bananacreampie
         kg = 1.0
      elif (object == 'r'): #obj is rock
         kg = 3.0
      elif (object == 'g'): #obj is gnome
         kg = 5.3
      elif (object == 'l'): #obj is light saber
         kg = 9.07
      else:
         kg = 0.0
      return kg
def getVelocityObject(distance):#takes the distance and gets the velocity of object
      gravity = 9.8
      velocityObject = sqrt((gravity*distance)/(2))
      return velocityObject
def getVelocitySkater(massSkater, massObject, velObject):#returns velocity of the skater by taking in 3 parameters
      velocitySkater = ((massObject * velObject)/(massSkater))
      return velocitySkater
