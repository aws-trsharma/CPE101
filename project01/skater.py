from funcs import *
from math import *
def main():
 #your code here
 weight = input("How much do you weigh (pounds)? ")
 distance = input("How far away is your professor (meters)? ")
 mass = input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ")
 mass = getMassObject(mass) 
 prof_resp= ''
 vel_resp = ''
 distance = float(distance)
 weight = float(weight)
 weight = poundsToKG(weight)
 vel_object = getVelocityObject(distance)
 vel_skater = getVelocitySkater(weight, mass, vel_object)
 if mass <= 0.1:
  prof_resp = "You're going to get an F!"
 elif mass > 0.1 and mass<=1.0 :
  prof_resp =  "Make sure your professor is OK."
 elif mass > 1.0:
   if distance < 20:
     prof_resp = "How far away is the hospital?"
   elif distance >= 20:
     prof_resp = "RIP professor."
   else:
      prof_resp = "error in code."
 print ("\nNice throw!", prof_resp)
 print ("Velocity of skater: %.3f m/s" % vel_skater)  
 if vel_skater  < 0.2:
  vel_resp = "My grandmother skates faster than you!"
  print(vel_resp)
 elif vel_skater >= 1.0:
  vel_resp = "Look out for that railing!!!"
  print(vel_resp)

if __name__ == '__main__':
 main()



