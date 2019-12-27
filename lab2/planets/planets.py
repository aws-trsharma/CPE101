def weight_on_planets():
   # write your code here
   weight = input("What do you weigh on earth? ")
   weight = float(weight)
   mars_weight = 0.38 * weight
   jupiter_weight = 2.34 * weight
   print("On Mars you would weigh %0.2f pounds.\nOn Jupiter you would weigh %0.2f pounds."
   % (mars_weight, jupiter_weight))
if __name__ == '__main__':
   weight_on_planets()
