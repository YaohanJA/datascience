
#  File: EasterSunday.py

#  Description: Cauculate Easter Sunday of a given year



def main():
  # prompt user to enter year
  y = int (input ("Enter year: "))
  2

  # compute a
  a = y % 19


  # compute b and c
  b = y // 100
  c = y % 100

  # do the rest of the computation
  d = b // 4
  e = b % 4
  g = ((8 * b) + 13) // 25
  h = ((19 * a) + b - d - g + 15) % 30
  j = c // 4
  k = c % 4
  m = (a + (11 * h)) // 319
  r = ((2 * e) + (2 * j) - k - h + m + 32) % 7
  n = ( h - m + r + 90) // 25
  p = ( h - m + r + n + 19) % 32



  # print the output
  print (" ")
  
  if (n == 1):
    print ("In", y, "Easter Sunday is on", p, "January.")
    
  if (n == 2):
    print ("In", y, "Easter Sunday is on", p, "Februray.")
    
  if (n ==
      3):
    print ("In", y, "Easter Sunday is on", p, "March.")
    
  if (n == 4):

    print ("In", y, "Easter Sunday is on", p, "April.")

  if (n == 5):
    print ("In", y, "Easter Sunday is on", p, "May.")

  if (n == 6):
    print ("In", y, "Easter Sunday is on", p, "June.")
    
  if (n == 7):
    print("In", y, "Easter Sunday is on", p, "July.")

  if ( n==8 ):
    print("In", y, "Easter Sunday is on", p, "August.")

  if ( n==9 ):
    print("In", y, "Easter Sunday is on", p, "September.")

  if  (n==10) :
    print("In", y, "Easter Sunday is on", p, "October.")

  if ( n==11 ):
    print("In", y, "Easter Sunday is on", p, "November.")

  if ( n==12 ):
    print("In", y, "Easter Sunday is on", p, "December.")  
		

main()
