#  File: CalculatePI.py

#  Description: pi random


import math
import random
def computePI ( numThrows) :
    count = 0
    for i in range (0, numThrows + 1):
      xPos = random.uniform ( -1.0,1.0 )
      yPos = random.uniform ( -1.0,1.0 )  
      if math.hypot(xPos , yPos) < 1:
        count +=1
    return (4*count/numThrows)

def main():
    print("Computation of PI using Random Numbers")
    print()
    Calculated_PI = 0
    dif = Calculated_PI - math.pi
    for i in range ( 2,8 ):
        Calculated_PI = computePI (10**i)
        dif = Calculated_PI - math.pi
        print ("num = %-10d " % 10**i, end = "")
        print ( "Calculated PI = %8.6f" % Calculated_PI, end = "   " )
        print ("Difference = % +.6f" %dif)
    print()    
    print ("Difference = Calculated PI - math.pi")    
main()    
        
        
