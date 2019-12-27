from quakeFuncs import *

def main():
      quakes = read_quakes_from_file("quakes.txt")
      def quitWrite(quakes):
         outFile = open('quakes.txt', 'w')
         for quake in quakes:
             outFile.write(repr(quake) + "\n")
      def printQuakes(quakes):
           print()
           print("Earthquakes:")
           print("------------")
           for quake in quakes:
              print (quake)
           print()
      printQuakes(quakes)
      while(len(quakes) > 0):
          print("Options:")
          print("  (s)ort")
          print("  (f)ilter")
          print("  (n)ew quakes")
          print("  (q)uit")
          print()
          user = input("Choice: ")
          if (user == "f" or user == "F"):
             secondin = input("Filter by (m)agnitude or (p)lace? ")
             if (secondin == "m" or secondin == "M"):
               lowerbound = float(input("Lower bound: "))
               upperbound = float(input("Upper bound: "))
               mag_quakes = filter_by_mag(quakes,lowerbound,upperbound)
               printQuakes(mag_quakes)
             elif (secondin == "p" or secondin == "P"):
               word = input("Search for what string? ")
               place_quakes = filter_by_place(quakes, word)
               printQuakes(place_quakes)
          elif (user == "s" or user =="S"):
             secondin = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ")
             if (secondin == "m" or secondin == "M"):
                 quakes.sort(key = attrgetter('mag'),reverse = True)
                 printQuakes(quakes)
             elif (secondin == "t" or secondin == "T"):
                 quakes.sort(key = attrgetter('time'),reverse = True)
                 printQuakes(quakes)
             elif (secondin == "l" or secondin == "L"):
                 quakes.sort(key = attrgetter('longitude'))
                 printQuakes(quakes)
             else:
                 quakes.sort(key = attrgetter('latitude'))
                 printQuakes(quakes)
          elif (user == "n" or user  == "N"):
              url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson'
              array = get_json(url)
              features = array["features"]
              count = 0
              for feature in features:
                 new_quake = quake_from_feature(feature)
                 if new_quake not in quakes:
                    quakes.append(new_quake)
                    count += 1
              if (count > 0):
                 print()
                 print("New quakes found!!!")
              printQuakes(quakes)
                    
          elif(user == "q"):
                quitWrite(quakes)
                break









if __name__ == '__main__':
   main()
