#  File: Goldbach.py

#  Description:

#  Student Name: Yaohan Jiang   

#  Student UT EID: yj3948

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: Oct. 10

#  Date Last Modified:

def is_prime (num):
  divisor = 2
  limit = int (num ** 0.5) + 1
  is_prime = True
  while (divisor < limit) and is_prime:
    if (num % divisor == 0):
      is_prime = False
    divisor = divisor + 1
  return is_prime

def main():
  a = eval(input("Enter the lower limit: "))
  while a < 4 or a % 2 != 0:
    a = eval(input("Enter the lower limit: "))
  b = eval(input("Enter the upper limit: "))
  while a > b or b %2 !=0:
    b = eval(input("Enter the upper limit: "))
  for num in range (a, b+1, 2):
      print (num, end = " ")
      for i in range (2, num):
          if is_prime(i):
              c = num - i
              if is_prime(c) and i <= c :
                  print("=", i, "+", c, end = " ")
      print()
main()                  
     
      
    


